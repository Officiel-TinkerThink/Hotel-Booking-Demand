# Hotel-Booking-Demand

# Hotel Booking Demand Prediction with Business Context

## Introduction

In the digital age, the hospitality industry has experienced a significant transformation. The rise of online booking platforms has revolutionized how travelers reserve their accommodations, offering unprecedented convenience and accessibility. However, while these platforms have opened up new markets and increased bookings, they also present significant challenges for hotel business owners.

## Problem

The ease of cancellation, while beneficial for customers, presents significant challenges for hotel business owners. These challenges include revenue instability and increased operational costs. Hotel owners are facing the problem of how to reduce the costs related to booking cancellations.

## Goal

Given the disadvantages or costs of booking cancellations, we aim to build a machine learning model capable of predicting bookings that are potentially likely to be canceled. By doing this, we can prevent or mitigate the negative impact caused by booking cancellations.

## Analytical Approach

We will analyze the pattern of cancellations among features we have based on previously recorded data labeled as either canceled or not canceled. We will then build a model that best classifies the bookings into two possible outcomes.

## Metric Evaluation

In our problem context, we will focus on recall while also considering the F2 score. Here's why:

- **Recall**: If a booking that is likely to be canceled is missed (false negative), it can lead to empty rooms and lost revenue. High recall ensures that most cancellations are correctly identified, even if it means having more false positives.
- **F2 Score**: This metric gives more weight to recall. It is particularly useful if the business impact of missed cancellations (false negatives) is significantly higher than the impact of falsely predicted cancellations (false positives). Using the F2 score ensures that the model prioritizes identifying as many cancellations as possible.

## Conclusion

From the hyperparameter tuning process, we determined that the best parameters for the Random Forest model are as follows:

- `n_estimators=125`
- `min_samples_split=3`
- `min_samples_leaf=2`
- `max_depth=10`
- `criterion="entropy"`
- `class_weight={0: 1, 1: 3}`
- `Threshold = 0.39`

The evaluation metrics scores are as follows:
- **F2 Score**: 0.793
- **Recall Score**: 0.937

The model helps reduce the financial risk due to costs related to cancellations by about 74.4%. This helps stabilize the hotel's financial balance. Non-refundable bookings were identified as a critical parameter in predicting cancellations.

## Further Analysis

The author assumes several things in this case:
- **Flat Price per Night**: Prices vary depending on the season and type of reserved room. This should be addressed in more in-depth analysis.
- **Impact of False Positives**: Estimated at $50 in numerical value, this oversimplification underestimates the effect on customer satisfaction and long-term hotel reputation. This should be included in further analysis.
- **Neglecting the Deposit**: The company receives money due to deposits, which should also be included when calculating the cost of cancellations.

## Recommendations

- **Focus on Recall and F2 First**: Initially, prioritize recall and F2 score, but later shift focus to the F1 score.
- **Incentives for Early Cancellation**: Offer incentives for early cancellations to manage booking and occupancy more effectively.

### Data

- **data_hotel_booking_demand.csv**: the dataset for the machine to learn to build model
- **data_test**: the dataset for the machine to predict in deployment

### Notebooks

- **main.ipynb**: Jupyter notebook for data analysis and model training.
- **deployment.ipynb**: Jupyter notebook for deployment and predict data test.

### Source code

- **ufunc.py**: Script for dependent function for data preprocessing.
- **models/**: Contains model and model_transformer generated during analysis.

### Reports
- [Presentation Video](https://drive.google.com/file/d/18M2Y1ZwpKjwqCRrV6nhswizwmpNW0G3G/view?usp=sharing)
- [Power Point Document](https://drive.google.com/file/d/1KqR5SqcH_6qbOps70QpGeba8XBds_bLc/view?usp=sharing)

### Other Files

- **README.md**: Project description and instructions.
- **requirements.txt**: List of required Python packages.
- **Hotel Booking Demand.pdf**: Script for data dictionary.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/hotel-booking-demand-prediction.git
   cd hotel-booking-demand-prediction

