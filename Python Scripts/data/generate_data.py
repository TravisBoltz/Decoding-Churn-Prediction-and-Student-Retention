import random
import pandas as pd

# Define lists for different fields
genders = ['Male', 'Female']
colleges = ['College of Engineering', 'College of Humanities and Social Sciences', 'College of Agriculture and Natural Resources', 'College of Art and Built Environment', 'College of Science', 'College of Health Sciences']
churns = ['Yes', 'No']
levels = [100, 200, 300, 400, 500]  # Removed 600
residences = ['Off-campus', 'On-campus']
sim_usage = ['Yes', 'No']
usage_frequency = ['Daily', 'Several times a week', 'Occasionally', 'Rarely', 'Never']
network_strength = [1, 2, 3, 4, 5]
services_used = ['Voice Calls', 'Mobile data/Internet', 'SMS/Text messaging']
data_allowance_exhaustion = ['Yes', 'No']
other_networks = ['Yes', 'No']
considered_discontinuing = ['Yes', 'No']
reasons_for_discontinuing = ['Poor network quality/coverage', 'Insufficient data allowance', 'Unsatisfactory customer service', 'High costs/pricing']
education_levels = ['Undergraduate', 'Postgraduate', 'Distant Learning', 'Masters', 'PhD']
monthly_data = ['0-2', '2-4', '4-6', '6-8', '8 and more']

# Define a function to generate synthetic responses
def generate_responses(num_responses_per_college):
    responses = []
    for college in colleges:
        for _ in range(num_responses_per_college):
            gender = random.choices(genders, weights=[0.442, 0.558], k=1)[0]
            churn = random.choices(churns, weights=[0.16, 0.84], k=1)[0]
            education_level = random.choices(education_levels, weights=[0.99, 0.000, 0.000, 0.0005, 0.00005], k=1)[0]

            if education_level in ['Postgraduate', 'Distant Learning', 'Masters', 'PhD']:
                level = random.choice([100, 200])
            else:
                if college in ['College of Science', 'College of Humanities and Social Sciences']:
                    level = random.choices(levels, weights=[0.3, 0.3, 0.24, 0.14, 0.02], k=1)[0]  # Reduced weight for level 400
                else:
                    level = random.choices([100, 200, 300, 400], weights=[0.3, 0.3, 0.3, 0.1], k=1)[0]  # Reduced weight for level 400

            residence = random.choices(residences, weights=[0.679, 0.321], k=1)[0]
            sim_usage_value = random.choices(sim_usage, weights=[0.96, 0.04], k=1)[0]
            usage_frequency_value = random.choices(usage_frequency, weights=[0.494, 0.16, 0.21, 0.049, 0.086], k=1)[0]
            network_strength_value = random.choices(network_strength, weights=[0.25, 0.247, 0.333, 0.086, 0.025], k=1)[0]
            voice_calls_value = random.choices(['Yes', 'No'], weights=[0.815, 0.185], k=1)[0]
            mobile_data_internet_value = random.choices(['Yes', 'No'], weights=[0.84, 0.16], k=1)[0]
            sms_text_messaging_value = random.choices(['Yes', 'No'], weights=[0.51, 0.48], k=1)[0]
            data_allowance_exhaustion_value = random.choices(data_allowance_exhaustion, weights=[0.827, 0.173], k=1)[0]
            other_networks_values = random.choices(other_networks, weights=[0.938, 0.062], k=1)[0]
            considered_discontinuing_value = random.choices(considered_discontinuing, weights=[0.84, 0.16], k=1)[0]

            poor_network_quality_coverage = 'Yes' if churn == 'No' else random.choices(['Yes', 'No'], weights=[0.704, 0.296], k=1)[0]
            insufficient_data_allowance = 'Yes' if churn == 'No' else random.choices(['Yes', 'No'], weights=[0.3, 0.7], k=1)[0]
            unsatisfactory_customer_service = 'Yes' if churn == 'No' else random.choices(['Yes', 'No'], weights=[0.39, 0.61], k=1)[0]
            high_costs_pricing = 'Yes' if churn == 'No' else random.choices(['Yes', 'No'], weights=[0.545, 0.455], k=1)[0]

            monthly_data_usage = random.choices(monthly_data, weights=[0.05, 0.1, 0.15, 0.2, 0.5], k=1)[0]

            responses.append([gender, college, churn, level, education_level, residence, sim_usage_value, usage_frequency_value, network_strength_value, voice_calls_value, mobile_data_internet_value, sms_text_messaging_value, data_allowance_exhaustion_value, other_networks_values, considered_discontinuing_value, poor_network_quality_coverage, insufficient_data_allowance, unsatisfactory_customer_service, high_costs_pricing, monthly_data_usage])

    return responses

# Generate synthetic responses for 768 students (128 per college)
num_responses_per_college = 128
responses = generate_responses(num_responses_per_college)

# Create a DataFrame from the synthetic responses
columns = ['Gender', 'College', 'Churn', 'Level', 'Education_Level', 'Residence', 'SIM_Usage', 'Usage_Freq', 'Network_Strength', 'Voice_Calls', 'Mobile_Data_Internet', 'SMS_Text_Messaging', 'Data_Exhaustion', 'Multiple_Networks','Other_Networks_Better_Services', 'Poor_Network_Quality_Coverage', 'Insufficient_Data_Allowance', 'Unsatisfactory_Customer_Service', 'High_Costs_Pricing', 'Monthly_Data_Usage']

data = pd.DataFrame(responses, columns=columns)

# Display the DataFrame
data

# Optional: Save the synthetic responses to a CSV file
data.to_csv('newData.csv', index=False)