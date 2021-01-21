import sys
from timeit import default_timer
from typing import List

from ann import ArtificialNeuralNetwork
from bayesian_network import BayesianNetworkForDiseasePrediction
from get_known_list_from_str import get_known_list_from_str


def get_symptoms_from_user(known_symptoms: List):
    print(
        'Please enter your symptoms separated by spaces (e.g. "itching chills vomiting"): '
    )
    user_symptoms = input()
    user_entered_symptoms = get_known_list_from_str(user_symptoms, known_symptoms)
    while user_entered_symptoms is None:
        print("Please input your symptoms again")
        user_symptoms = input()
        user_entered_symptoms = get_known_list_from_str(user_symptoms, known_symptoms)
    return user_entered_symptoms


if __name__ == "__main__":
    try:
        option = sys.argv[1]
        if option == "-bayesnet":
            BayesianNetworkForDiseasePrediction(
                get_symptoms_from_user
            ).predict_with_known_dataset()
        elif option == "-bayesnet_from_file":
            try:
                file_name = sys.argv[2]
                BayesianNetworkForDiseasePrediction(
                    get_symptoms_from_user
                ).predict_from_data(file_name)
            except IndexError:
                raise SystemExit(
                    f"Usage: {sys.argv[0]} {option} [filename]\nUse {sys.argv[0]} -h for help"
                )
        elif option == "-ann":
            if __name__ == "__main__":
                program_start = default_timer()
                ann = ArtificialNeuralNetwork()
                x, y = ann.data_sweep()
                x_train, x_test, y_train, y_test = ann.ann_train_test_split(x, y)
                ann.ann_training(x_train, x_test, y_train, y_test)
                program_end = default_timer()
                print(
                    f"The ANN implementation completed in {program_end - program_start} seconds"
                )
        elif option == "-h":
            print(
                f"Usage: {sys.argv[0]} [option]\n"
                f"Options and arguments:\n"
                f"-h: Help menu\n"
                f"-bayesnet : Uses Bayesian Network algorithm\n"
                f"-bayesnet_from_file filename : Uses Bayesian Network Algorithm with samples in the csv folder under the given filename\n"
                f"-ann : Uses Artificial Neural Network algorithm"
            )
        else:
            print(
                f"You must call this function with arguments\n"
                f"Use {sys.argv[0]} -h for help"
            )
    except IndexError:
        raise SystemExit(
            f"Usage: {sys.argv[0]} [option]\nUse {sys.argv[0]} -h for help"
        )
