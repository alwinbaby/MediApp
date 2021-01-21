# Medi-App

A python application for the self-diagnosis of illnesses, utilizing two implementations for prediction: a Bayesian Network and an Artificial Neural Network with Multi-Layer Perceptron.

***

## Project Summary

Medi-App provides the symptom-to-illness investigation of online clinical databases without the time consumption of searching online. Symptoms and illness prognosis data are from online machine learning database Kaggle (Anonymous, 2020) under the Database Contents License v1.0, and are fit for our purpose of academic use. The data are used to train a Bayesian Network (Bayes's Net) and an Artificial Neural Network (ANN) with Multi-Layer Perceptron (MLP). The resulting probabilistic models provide Medi-App with the capability to compare user symptoms with past observed symptoms, and report the probability that the user is observing symptoms that indicate the presence of a particular illness or disease.

Anonymous (Nirma University) (2020). Disease Prediction Using Machine Learning (Version 1) [Data set]. Kaggle. https://www.kaggle.com/kaushil268/disease-prediction-using-machine-learning

## Project Proposed

Our team aimed to create an application to support the self-diagnosing of illnesses; where users of the application do not need to search through clinical websites such as [Mayo Clinic](www.mayoclinic.org) to investigate their possible mystery illness. Instead, we proposed that users enter their symptoms into the application to sort them out. We intended to use a reasonably fast and accurate artificial intelligence algorithm (within some example, educational allowance) to achieve legitimate results from the user’s input symptoms to the suggested output illnesses.

 We investigated three state-of-the-art approaches for our purpose: 
 1. utilizing the Bayesian network probabilistic graphical model: with a test set of data representing the probability of a particular symptom relating to a particular illness;
 2. creating an Artificial Neural Network (ANN): with some naive function for the hidden layer representing the same probability;
 3. and k-means clustering: where each additional user’s input is a means to train the program without the need for existing legitimate medical data
 
 There exists several academic journals related to using our investigation algorithms above, notable ones related to our project include:
 1. Auras, H., Merouani, H. F., & Refai, A. (2016). Maintenance of a Bayesian network: application using medical diagnosis. Evolving Systems, 7(3), 187-196. doi: 10.1007/s12530-016-9146-8. https://casls-primo-prod.hosted.exlibrisgroup.com/permalink/f/1ed24l6/TN_cdi_crossref_primary_10_1007_s12530_016_9146_8
 2. Govrdhan, A., Kavihta Rani, B., & Srinivas, K. (2010). Applications of Data Mining Techniques in Healthcare and Prediction of Heart Attacks. International Journal on Computer Science and Engineering, 2(2), 250-255. https://www.researchgate.net/profile/Dr_Govardhan/publication/49617135_Applications_of_Data_Mining_Techniques_in_Healthcare_and_Prediction_of_Heart_Attacks/links/5435156d0cf2dc341daf6a8e.pdf
 3. Abdalla, A., Alashwal, H., Crouse, J., El Halaby, M., & Moustafa, A. (2019). The Application of Unsupervised Clustering Methods to Alzheimer’s Disease. Frontiers in Computational Neuroscience, 13, 31. https://dx.doi.org/10.3389%2Ffncom.2019.00031 

Each journal above investigates a portion of which we wished to acheive:
1. Bayesian networks readily resolve our foreseen issue regarding the different chances that some set of symptoms is related to a particular illness: we would have been able to exploit the probabilistic model the algorithm represents and report the chances of a particular illness.

The article by Auras, et. al (2016) presents the use of a Bayesian Network in the diagnosis of breast-related diseases using legitimate medical data. However, we do not have the same access to legitimate medical data and as such needed to investigate datasets for training the Bayesian Network.

2. Similarly to Bayesian networks, an ANN provide us with a model that connects symptoms to illnesses. Additionally, the strucutre of ANN allows us to correct probabilities by comparing the ANN computed illness to the actual illness confirmed by the user and then adjusting the ANN structure.

The article by Govrdhan, et. al (2010) presents the use of an ANN when mining medical data for the prediction of heart attacks. The system is first built using data and then is training on new data as it arrives. Again, as we did not have access to legitimate medical data our ANN could have been training on arriving data only.

3. Similar to the algorithms above, k-means clustering provides us with a model that can be used to predict input-to-output relationships. Interestingly, the model is not based on probability statistics and instead is used to find natural groupings between inputs as the algorithm executes. We could compare the clusters of symptoms to known sets of symptoms-to-illness from reputable clinical websites and report.

The article by Abdalla, et. al (2019) investigates the use of k-means clusters to determine the symptoms of Alzheimer’s disease to better predict that a group of symptoms is predictive of the disease. K-means clustering, like Bayesian networks, usually operates from an initial set of data - however, as the k-means clustering does not need the probabilities of symptoms to illness we could have used legitimate sypmtoms-to-illness relationship data as our first training set.

As we, the team are not medical professionals we do not have accurate and legitimate symptoms-to-illness relationship data at our disposal. We intended to retrieve legitimate data (or as close as possible data) from reputable clinical databases under a license that allows us to use the data for academic purposes.

## Project Deliverables 

The deliverables assigned and set out by our post-seconday software engineering course are as follows:
1. [Project Proposal](https://github.com/holtzmak/Medi-App/blob/main/documentation/Project%20Proposal.pdf) (September 25, 2020)
1. [Project Progress Report](https://github.com/holtzmak/Medi-App/blob/main/documentation/Project%20Progress%20Report.pdf) (October 30, 2020)
1. [Project Final Report](https://github.com/holtzmak/Medi-App/blob/main/documentation/Project%20Final%20Report.pdf) (December 4, 2020)
1. [Poster](https://github.com/holtzmak/Medi-App/blob/main/documentation/Poster.pdf) (December 6, 2020)
1. [Presentation Slides](https://github.com/holtzmak/Medi-App/blob/main/documentation/Presentation%20Slides.pdf) (December 6, 2020)

***

## Legal Notices

This project is not affiliated with nor endorsed by any medical agency. The project is presented for academic investigation purposes only.

>This is free and unencumbered software released into the public domain.
>
>Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.
>
>In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
>
>For more information, please refer to https://unlicense.org
