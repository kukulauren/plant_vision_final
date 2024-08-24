# API Documentation
## Overview
This documentation covers three APIs for different functionalities. To use these APIs, follow the instructions provided.

## Base URL
To determine the base URL for your APIs:
- Run run.py in your terminal.
- The output will include the base URL to be used (e.g., http://10.0.0.10:8000/).

## Authentication
Authentication is not yet implemented.

## Getting Started
> [!WARNING]
> Please start here.
Quick Start Guide
- Install the required packages by running:
  ```
  pip install -r requirements.txt
  ```
- Start the local servers by executing:
  ```
  python3 run.py
  ```
  Here, two local servers (base URLs) will be provided. Test the APIs using Postman or any other API testing tool.

API Endpoints
1. Plant Disease Identification
- Base URL: http://127.0.0.1:8000/
- Endpoint: /plant/get
- Method: POST
- Request:
- Content-Type: Form-data
- Key: image
- Value: Image file (upload the image file to test)
- Response will be as follows.
- {
      "prediction": "Potato___Early_blight"
  }
2. Crop Recommendation
- Base URL: http://192.168.1.2:8000/
- Endpoint: /recommend/get
- Method: POST
- Request:
- Content-Type: Raw JSON
- Body:
- {
      "features": [90, 42, 43, 20.879744, 82.00274, 6.50298, 202.935536]
  }
- Response will be as follows.
- {
    "prediction": "rice"
  }
3. Chat Model
- Base URL: http://192.168.1.2:8000/
- Endpoint: /chat/get
- Method: POST
- Request:
- Content-Type: Raw JSON
- Body:
- {
  "msg": "ဆီအုန်းစိုက်ပျိုးရေးအကြောင်းရှင်းပြပါ"
  }
- Response will be as follows.
- {
    "response": "ဆီအုန်းသည် အပူပိုင်းဒေသများတွင် စိုက်ပျိုးသော အခိုင်အမာသစ်ပင်ဖြစ်ပြီး အလွန်မိုးလေဝသလည်းလိုအပ်သည်။ ၎င်း၏ အခြေခံအာဟာရတွင် အဆီအဓိပ္ပါယ်ရှိပြီး နေ့စဉ်အသုံးပြုသော ထုတ်ကုန်များတွင် အရေးပါသည်။ ဆီအုန်းကို စိုက်ပျိုးရာတွင် မြေအမျိုးအစားနှင့် အခြေအနေများကို အထူးဂရုစိုက်သင့်ပါသည်။"
  }

# User Input Guidelines
When getting users' input values, it's important to adhere to specified ranges to ensure the model operates correctly. Below are guidelines for maintaining valid input ranges:

### Ways to do input Ranges and Validation
1. Slider Bars
- Description: Use slider bars to select values within the specified range for model parameters.
- Example: For the parameter K, set the slider within the range of 5 to 205.
- Implementation: Adjust slider bars to ensure that input values fall within the acceptable range.
2. Additional Information and Input Constraints
- Description: Provide additional information or instructions above the input boxes to help users maintain valid input values.
- Example:
- For parameter K, display a message like "Value must be between 5 and 205" above the input field.
- Validate the input to ensure it falls within the specified range before processing(checking conditions).
**Input features should be validated to match the expected range.**
**Example message: "Ensure feature values are between [min_value, max_value]."**
> [!IMPORTANT]
> You can check the valid values for N,P,K,temperature,humidity, ph, rainfall in the rows of min and max. 
<img width="1024" alt="Screen Shot 2024-08-11 at 14 34 02" src="https://github.com/user-attachments/assets/02d5584b-26b7-49b8-b71a-7775fc082bab">
