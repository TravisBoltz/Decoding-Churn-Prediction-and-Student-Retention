import random
import string
import pandas as pd
import math

# Define lists for different fields
genders = ["Male", "Female"]
colleges = [
    "College of Engineering",
    "College of Humanities and Social Sciences",
    "College of Agriculture and Natural Resources",
    "College of Art and Built Environment",
    "College of Science",
    "College of Health Sciences",
]
churns = ["Yes", "No"]
levels = [100, 200, 300, 400, 500, 600]
residences = [
    "Off-campus",
    "On-campus",
]  # Increased probability of selecting 'Off-campus'
sim_usage = ["Yes", "No"]
usage_frequency = [
    "Daily",
    "Several times a week",
    "Occasionally",
    "Rarely",
    "Never",
]  # Decreased probability of selecting 'Rarely' and 'Never'
network_strength = [1, 2, 3, 4, 5]
services_used = ["Voice Calls", "Mobile data/Internet", "SMS/Text messaging"]
data_allowance_exhaustion = ["Yes", "No"]
other_networks = ["Yes", "No"]  # Increased probability of selecting 'Yes'
considered_discontinuing = ["Yes", "No"]
reasons_for_discontinuing = [
    "Poor network quality/coverage",
    "Insufficient data allowance",
    "Unsatisfactory customer service",
    "High costs/pricing",
]


# Define a function to generate synthetic responses
def generate_responses(num_responses):
    responses = []
    for _ in range(num_responses):
        gender = random.choice(genders)
        college = random.choice(colleges)
        churn = random.choices(churns, weights=[0.7, 0.3], k=1)[
            0
        ]  # Decreased probability of selecting 'No'
        level = random.choices(
            levels,
            weights=[
                0.2,
                0.2,
                0.2,
                0.2,
                (
                    0.1
                    if college in ["College of Science", "College of Health Sciences"]
                    else 0.0
                ),
                (
                    0.1
                    if college in ["College of Science", "College of Health Sciences"]
                    else 0.0
                ),
            ],
            k=1,
        )[
            0
        ]  # Decreased probability of selecting 500 and 600, except for College of Science and College of Health Sciences
        residence = random.choices(residences, weights=[0.8, 0.2], k=1)[
            0
        ]  # Increased probability of selecting 'Off-campus'
        sim_usage_value = random.choice(sim_usage)
        usage_frequency_value = random.choices(
            usage_frequency, weights=[0.3, 0.3, 0.3, 0.05, 0.05], k=1
        )[
            0
        ]  # Decreased probability of selecting 'Rarely' and 'Never'
        network_strength_value = random.choice(
            network_strength
        )  # Network strength capped at 5
        voice_calls_value = random.choices(["Yes", "No"], weights=[0.8, 0.2], k=1)[0]
        mobile_data_internet_value = random.choices(
            ["Yes", "No"], weights=[0.8, 0.2], k=1
        )[0]
        sms_text_messaging_value = random.choices(
            ["Yes", "No"], weights=[0.8, 0.2], k=1
        )[0]
        data_allowance_exhaustion_value = random.choice(data_allowance_exhaustion)
        other_networks_values = random.choices(
            other_networks, weights=[0.85, 0.15], k=1
        )[
            0
        ]  # Increased probability of selecting 'Yes'
        considered_discontinuing_value = random.choices(
            considered_discontinuing, weights=[0.95, 0.05], k=1
        )[
            0
        ]  # Increased probability of selecting 'Yes'

        # Separate reasons for discontinuing into individual questions
        poor_network_quality_coverage = (
            "Yes"
            if churn == "Yes"
            else random.choices(["Yes", "No"], weights=[0.3, 0.7], k=1)[0]
        )
        insufficient_data_allowance = (
            "Yes"
            if churn == "Yes"
            else random.choices(["Yes", "No"], weights=[0.3, 0.7], k=1)[0]
        )
        unsatisfactory_customer_service = (
            "Yes"
            if churn == "Yes"
            else random.choices(["Yes", "No"], weights=[0.3, 0.7], k=1)[0]
        )
        high_costs_pricing = (
            "Yes"
            if churn == "Yes"
            else random.choices(["Yes", "No"], weights=[0.3, 0.7], k=1)[0]
        )

        monthly_data_usage = max(
            0.5, round(random.uniform(0.5, 10.0) + random.uniform(-0.5, 0.5), 2)
        )
        responses.append(
            [
                gender,
                college,
                churn,
                level,
                residence,
                sim_usage_value,
                usage_frequency_value,
                network_strength_value,
                voice_calls_value,
                mobile_data_internet_value,
                sms_text_messaging_value,
                data_allowance_exhaustion_value,
                other_networks_values,
                poor_network_quality_coverage,
                insufficient_data_allowance,
                unsatisfactory_customer_service,
                high_costs_pricing,
                monthly_data_usage,
            ]
        )

    return responses


# Estimate sample size for clustering sampling
population_size = 85000
desired_precision = 0.05  # +/- 5% margin of error
confidence_level = 0.95  # 95% confidence level
design_effect = 2  # Assuming a design effect of 2 for clustering sampling

# Calculate sample size
sample_size = int(design_effect * (1.96**2 * 0.5 * (1 - 0.5)) / (desired_precision**2))
print(
    f"Estimated sample size for clustering sampling with a population of {population_size}: {sample_size}"
)

# Generate synthetic responses
num_responses = sample_size
responses = generate_responses(num_responses)

# Create a DataFrame from the synthetic responses
columns = [
    "Gender",
    "College",
    "Churn",
    "Level",
    "Residence",
    "SIM_Usage",
    "Usage_Freq",
    "Network_Strength",
    "Voice_Calls",
    "Mobile_Data_Internet",
    "SMS_Text_Messaging",
    "Data_Exhaustion",
    "Other_Networks",
    "Poor_Network_Quality_Coverage",
    "Insufficient_Data_Allowance",
    "Unsatisfactory_Customer_Service",
    "High_Costs_Pricing",
    "Monthly_Data_Usage",
]

df = pd.DataFrame(responses, columns=columns)
df

# Save the synthetic responses to a CSV file
# df.to_csv('reData.csv', index=False)
