import itertools
import operator
from timeit import default_timer
from typing import Callable, List, OrderedDict

import pandas
from get_from_csv import get_from_csv
from pomegranate import (
    DiscreteDistribution,
    ConditionalProbabilityTable,
    Node,
    BayesianNetwork,
)


class BayesianNetworkForDiseasePrediction:
    def __init__(self, get_symptoms_from_user: Callable):
        self.get_symptoms_from_user = get_symptoms_from_user

    def predict_from_data(self, samples_file_name: str):
        """
        This function will predict diseases from symptoms using a given dataset with an expected structure.
        The dataset structure must be in the format of symptoms in columns 0 to last-1 and diseases in the last column.
        :param samples_file_name: the name of the csv_file in the csv folder
        :return: None
        """
        program_start_before_input = default_timer()
        samples = pandas.read_csv(
            f"../csv/{samples_file_name}.csv", delimiter=",", header=None
        )
        program_end_before_input = default_timer()
        user_symptoms = self.__get_symptoms_from_user(samples)
        program_start_after_input = default_timer()
        number_symptoms = samples.shape[1] - 1  # number columns in samples
        model_start_time = default_timer()
        model = BayesianNetwork.from_samples(
            X=samples.values,
            include_edges=[
                (symptom, number_symptoms) for symptom in range(number_symptoms)
            ],
            exclude_edges=(
                list(
                    itertools.combinations(
                        [symptom for symptom in range(number_symptoms)],
                        2,
                    )
                )
            ),
        )
        model.bake()
        model_end_time = default_timer()
        print(
            f"Model finished construction in {model_end_time - model_start_time} seconds"
        )
        predicted_disease = model.predict([user_symptoms])[0]
        prediction_probability = model.probability([predicted_disease])
        print(
            f"The predicted disease is {predicted_disease[-1]} with probability of {prediction_probability}"
        )
        program_end_after_input = default_timer()
        full_program_runtime = (
            program_end_before_input - program_start_before_input
        ) + (program_end_after_input - program_start_after_input)
        print(
            f"The Bayes's Net implementation completed in {full_program_runtime} seconds"
        )

    def __get_symptoms_from_user(self, samples):
        values_from_samples_with_duplicates = pandas.DataFrame(samples).to_dict(
            orient="list"
        )
        values_from_samples = list()
        for _, values in itertools.islice(
            values_from_samples_with_duplicates.items(),
            len(values_from_samples_with_duplicates.items()) - 1,
        ):
            values_from_samples = values_from_samples + list(
                OrderedDict.fromkeys(values)
            )
        user_reported_symptoms = self.get_symptoms_from_user(values_from_samples)
        inferred_symptoms = list()
        for symptom in list(values_from_samples):
            if symptom in user_reported_symptoms:
                inferred_symptoms.append(symptom)
            else:
                if not symptom.startswith("not_"):
                    inferred_symptoms.append(f"not_{symptom}")
        inferred_symptoms.append(None)  # To infer the disease
        return inferred_symptoms

    # TODO: Make agnostic to symtoms, diseases, filename, etc.
    def predict_with_known_dataset(self):
        """
        This function will predict diseases from symptoms using a known dataset and known structure.
        :return: None
        """
        known_symptoms = get_from_csv("Symptom Probability Tables")
        user_symptoms = self.__get_known_symptoms(known_symptoms)
        (
            symptom_distributions,
            symptom_states,
        ) = self.__get_symptom_distributions_and_states(known_symptoms)
        bayesian_networks_of_diseases = list()
        for disease in [
            "Acne",
            "Allergy",
            "Chicken Pox",
            "Common Cold",
            "Drug Reaction",
            "Psoriasis",
        ]:
            bayesian_networks_of_diseases.append(
                self.__get_bayesian_network_model(
                    symptom_distributions=symptom_distributions,
                    symptom_states=symptom_states,
                    file_name=f"{disease} Full Conditional Probability Table",
                    disease_name=disease,
                )
            )
        prediction_results = dict()
        for bayes_net in bayesian_networks_of_diseases:
            symptoms_and_disease_to_predict = list()
            for s in user_symptoms.values():
                symptoms_and_disease_to_predict.append(
                    f"{s}"  # Requires string per API
                )
            symptoms_and_disease_to_predict.append(
                "1"  # Predict the disease as present
            )
            prediction_results[bayes_net.name] = bayes_net.probability(
                [symptoms_and_disease_to_predict]
            )
        print(
            "Top 3 predicted diseases are (disease, probability):",
            sorted(
                prediction_results.items(), key=operator.itemgetter(1), reverse=True
            )[:3],
        )

    # TODO: Make agnostic to number symptoms
    def __get_known_symptoms(self, known_symptoms: List):
        user_symptoms = self.get_symptoms_from_user(
            [s for s, _, _, _ in known_symptoms]
        )
        symptom_dict = dict()
        for symptom, _, _, _ in known_symptoms:
            symptom_dict[symptom] = 1 if symptom in user_symptoms else 0
        return symptom_dict

    # TODO: Make agnostic to symptoms
    def __get_symptom_distributions_and_states(self, known_symptoms: List):
        symptom_distributions = list()
        symptom_states = list()
        for (
            symptom,
            probability,
            not_symptom,
            not_probability,
        ) in known_symptoms:
            symptom_distribution = DiscreteDistribution(
                {"1": float(probability), "0": float(not_probability)}
            )
            symptom_distributions.append(symptom_distribution)
            symptom_states.append((Node(symptom_distribution, name=symptom)))
        return symptom_distributions, symptom_states

    # TODO: Make agnostic to number symptoms
    def __get_bayesian_network_model(
        self,
        symptom_distributions: List,
        symptom_states: List,
        file_name: str,
        disease_name: str,
    ):
        disease_conditional_distribution = list()
        for (s1, s2, s3, s4, s5, d, p) in get_from_csv(file_name):
            disease_conditional_distribution.append([s1, s2, s3, s4, s5, d, float(p)])
        disease_distribution = ConditionalProbabilityTable(
            disease_conditional_distribution,
            symptom_distributions,
        )
        disease = Node(disease_distribution, name=disease_name)
        model = BayesianNetwork(disease_name)
        model.add_state(disease)
        for symptom_state in symptom_states:
            model.add_state(symptom_state)
            model.add_edge(symptom_state, disease)
        model.bake()
        return model
