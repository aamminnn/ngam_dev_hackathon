import pandas as pd 
import random 
from faker import Faker 

# Initialize Faker 
fake = Faker() 

# Possible specializations and languages 
specializations = ["Family Law", "Corporate Law", "Criminal Law", "Intellectual Property", "Contract Law", "Employment Law"] 
languages = ["English", "Malay", "Mandarin", "Tamil"] 

# Generate synthetic data 
data = [] 
for i in range(10):  # 10k lawyers 
    lawyer_id = i + 1 
    name = fake.name() 
    # specialization = random.choice(specializations) 
    progress = random.randint(1, 400) 
    quality = random.randint(1, 10)
    impact = random.randint(1, 10)
    complexity = random.randint(1, 10)
    timeliness = random.randint(1, 10)
    # impact = round(random.uniform(0.1, 0.95), 2)  # between 40% - 95% 
    # location = fake.city() 
    # lang_spoken = random.sample(languages, random.randint(1, 2))  # 1-2 languages 
    # rating = round(random.uniform(2.5, 5.0), 1)  # client rating 

    data.append([lawyer_id, name, progress, quality, impact, complexity, timeliness]) 

# Convert to DataFrame 
# df = pd.DataFrame(data, columns=[ 
#     "lawyer_id", "name", "specialization", "years_experience",  
#     "cases_handled", "success_rate", "location", "languages", "rating" 
# ]) 

df = pd.DataFrame(data, columns=[ 
    "emp_id", "emp_name", "progress", "quality",  "impact", "complexity", "timeliness" 
]) 

# Add score column using your weights
df["score"] = (
    0.2*df["progress"] +
    0.3*df["quality"] +
    0.25*df["impact"] +
    0.15*df["complexity"] +
    0.1*df["timeliness"]
)

# Save to CSV 
df.to_csv("test_data.csv", index=False) 
print(df.head(10))  # preview first 10 rows 

# df = pd.read_csv("emp_data.csv")
# # Save back to CSV
# # df.to_csv("emp_data.csv", index=False)