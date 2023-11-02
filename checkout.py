import requests
import random
import threading
from flask import Flask, request, jsonify
import time
import sys
from datetime import datetime, timedelta
import multiprocessing

app = Flask(__name__)

stop_event = threading.Event()
api_processes = []

# Add a flag to track the stop request
stop_requested = False

def generate_random_first_name():
    names = ["James", "John", "Robert", "Michael", "William", "David", "Adams", "Mary", "Jennifer", "Linda", "Patricia", "Elizabeth"]
    random_first_name = random.choice(names)
    return random_first_name

def generate_random_last_name():
    names =["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson"]
    random_last_name = random.choice(names)
    return random_last_name

def generate_random_amount(amount_floor, amount_ceiling, multiplier):
    return random.randint(amount_floor,amount_ceiling) *multiplier

def generate_random_card_number(card_success):
    if random.randint(1, 100) <= card_success:
        cards = [
            "4111111111111111",
            "2222400010000008",
            "2223520443560010",
            "4000160000000004",
            "4111111111111111",
            "2222400010000008",
            "2223520443560010",
            "4000160000000004"
        ]
    else:
        cards = [
            "370000000000002"
        ]
    random_card = random.choice(cards)
    return random_card

def generate_random_wallet():
    wallets = [
        "wallet/airtelmoney",
        "wallet/mobikwik", 
        "wallet/freechargewallet",
        "wallet/phonepe"
    ]
    random_wallet = random.choice(wallets)
    return random_wallet

def choose_transaction_type(distribution):
    random_value = random.uniform(0, 100)
    cumulative_percentage = 0
    for transaction_type, percentage in distribution.items():
        cumulative_percentage += percentage
        if random_value <= cumulative_percentage:
            return transaction_type
    return None


def checkout_loaded_api_call(api_key, session_token):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "CHECKOUT_LOADED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("CHECKOUT LOADED successfully.")

def user_authenticated_api_call(api_key, session_token):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "USER_AUTHENTICATED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("USER AUTHENTICATED successfully.")

def address_updated_api_call(api_key, session_token):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "ADDRESS_UPDATED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("ADDRESS UPDATED successfully.")

def payment_category_api_call(api_key, session_token):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "PAYMENT_CATEGORY_SELECTED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("PAYMENT CATEGORY SELECTED successfully.")

def payment_method_api_call(api_key, session_token,transaction_type):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "PAYMENT_METHOD_SELECTED",
        "eventAttrs": {
            "paymentType": transaction_type,
        }
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("PAYMENT METHOD SELECTED successfully.")

def payment_instrument_api_call(api_key, session_token):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "PAYMENT_INSTRUMENT_PROVIDED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("PAYMENT_INSTRUMENT_PROVIDED successfully.")

def payment_initiated_api_call(api_key, session_token,transaction_type,card_success, wallet_success, upi_success, bnpl_success):

    random_card = generate_random_card_number(card_success)
    random_wallet = generate_random_wallet()
    random_name_first = generate_random_first_name()
    random_name_last = generate_random_last_name()

    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": "PAYMENT_INITIATED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print("PAYMENT INITIATED successfully.")

    execute_session_url = f'https://test-apis.boxpay.tech/v0/checkout/sessions/{session_token}'  # Replace with your actual URL
    execute_session_headers = {
        'Content-Type': 'application/json',
        'X-Request-Id': 'weassjdr23',  # Replace with your X-Request-Id
    }

    upi_success = int(upi_success)
    if random.randint(1, 100) <= upi_success:
        shopperVpa = "test@boxpay"  # Transaction succeeds
    else:
        shopperVpa = "test-rejected@boxpay"
    
    wallet_success = int(wallet_success)
    if random.randint(1, 100) <= wallet_success:
        token = "test"  # Transaction succeeds
    else:
        token = "test-rejected"
        
    if transaction_type == 'Wallet':
        selected_instrument = {"type": random_wallet, "wallet": {"token": token}}
        
    if transaction_type == 'BuyNowPayLater':
        selected_instrument = {"type": "bnpl/afterpay", "wallet": {"token": token}}
        
    if transaction_type == 'Upi':
        selected_instrument = {"type": "upi/collect", "upi": {"shopperVpa": shopperVpa}}
        
    if transaction_type == 'Card':
        selected_instrument =     {"type": "card/plain", "card": {
        "number": random_card,
        "expiry": "2030-03",
        "cvc": "737",
        "holderName": "John Smith"
    }}
        
    execute_session_payload = {
        "browserData": {
            "browserLanguage": "en-US",
            "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "userAgentHeader": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "ipAddress": "123.123.123.123"
        },
        "instrumentDetails": selected_instrument,  # Randomly selected instrument details
        "shopper": {
             
            "email": "test123@gmail.com",
            "uniqueReference": "x123y",
            "phoneNumber": "+91123456789"
        },
        "billingAddress": {
            "address1": "first address line",
            "address2": "second address line",
            "city": "Faridabad",
            "state": "Haryana",
            "countryCode": "IN",
            "postalCode": "121004"
        }
    }
    

    response_execute_session = requests.post(execute_session_url, json=execute_session_payload, headers=execute_session_headers)
    response_data = response_execute_session.json()
    transaction_id = response_data.get('transactionId')
    
    if response_execute_session.status_code == 200:
        print("session executed successfully.")
    else:
        print("Payment Initiated API call failed with status code:", response_execute_session.status_code)

    return transaction_id

def payment_result_api_call(api_key, session_token):
    url_ui_analytics = 'https://test-apis.boxpay.tech/v0/ui-analytics'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    ui_analytics_payload = {
        "callerToken": session_token,
        "uiEvent": " PAYMENT_RESULT_SCREEN_DISPLAYED"
    }
    response_ui_analytics = requests.post(url_ui_analytics, json=ui_analytics_payload, headers=headers)
    if response_ui_analytics.status_code == 200:
        print(" PAYMENT_RESULT_SCREEN_DISPLAYED successfully.")


def execute_api_calls(api_url, api_key, amount_floor, amount_ceiling, multiplier, distribution, card_success, wallet_success, upi_success, bnpl_success):
    global session_loaded
    random_name_first = generate_random_first_name()
    random_name_last = generate_random_last_name()
    amount = generate_random_amount(amount_floor,amount_ceiling,multiplier)
    transaction_type = choose_transaction_type(distribution)
    url = api_url
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    payload = {
        "context": {
            "countryCode": "IN",
            "legalEntity": {
                "code": "legal_entity"
            },
            "orderId": "test12"
        },
        "paymentType": "S",
        "money": {
            "amount": amount,
            "currencyCode": "INR"
        },
        "shopper": {
            "firstName": random_name_first,
            "lastName": random_name_last,
            "email": "test123@gmail.com",
            "uniqueReference": "x123y",
            "phoneNumber": "+91123456789",
            "deliveryAddress": {
                "address1": "first address line",
                "address2": "second address line",
                "city": "Faridabad",
                "state": "Haryana",
                "countryCode": "IN",
                "postalCode": "121004"
            },
        },
        "frontendReturnUrl": "https://www.boxpay.tech",
        "frontendBackUrl": "https://www.boxpay.tech"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        data = response.json()
        session_token = data.get('token', 'Session token not found')
        print(f"Session Token: {session_token}")
        checkout_loaded_api_call(api_key, session_token)
        
        sleep_time = random.uniform(30,120)
        time.sleep(sleep_time)
        
        second_api_probability = random.uniform(0.95, 1)
        if random.random() <= second_api_probability:
            user_authenticated_api_call(api_key, session_token)

            sleep_time = random.uniform(30,120)
            time.sleep(sleep_time)

            third_api_probability = random.uniform(0.85, 0.95)
            if random.random() <= third_api_probability:
                address_updated_api_call(api_key, session_token)

                fourth_api_probability = random.uniform(0.95, 1)
                if random.random() <= fourth_api_probability:
                    payment_category_api_call(api_key, session_token)

                    sleep_time = random.uniform(30,120)
                    time.sleep(sleep_time)

                    fifth_api_probability = random.uniform(0.95, 1)
                    if random.random() <= fifth_api_probability:
                        payment_method_api_call(api_key, session_token,transaction_type)

                        sixth_api_probability = random.uniform(0.90, 1)
                        if random.random() <= sixth_api_probability:
                            payment_instrument_api_call(api_key, session_token)

                            sleep_time = random.uniform(30,120)
                            time.sleep(sleep_time)

                            seventh_api_probability = random.uniform(0.85, 0.98)
                            if random.random() <= seventh_api_probability:
                                transaction_id = payment_initiated_api_call(api_key, session_token,transaction_type,card_success, wallet_success, upi_success, bnpl_success)

                                eighth_api_probabality = random.uniform(0.90, 0.95)
                                if random.random() <= eighth_api_probabality:
                                    payment_result_api_call(api_key, session_token)
                                    session_loaded = True  # Set the flag to indicate session loaded
                                else:
                                    print("Eighth API call skipped")
                            else:
                                print("Seventh API call skipped.")
                        else:
                            print("Sixth API call (PAYMENT_INITIATED) skipped.")
                    else:
                        print("Fifth API call (PAYMENT_METHOD_SELECTED) skipped.")
                else:
                    print("Fourth API call (PAYMENT_CATEGORY_SELECTED) skipped.")
            else:
                print("Third API call (ADDRESS_UPDATED) skipped.")
        else:
            print("Second API call (USER_AUTHENTICATED) skipped.")
    else:
        print(f"First API call failed with status code: {response.status_code}")
        print(response.text)
    
    if random.randint(1, 100) <= 10:
        refund_transaction(transaction_id, amount)
    

def repeat_api_calls(api_url, api_key, amount_floor, amount_ceiling, multiplier, distribution, card_success, wallet_success, upi_success, bnpl_success):
    global stop_requested

    while not stop_event.is_set():
        if stop_requested:
            break
        execute_api_calls(api_url, api_key, amount_floor, amount_ceiling, multiplier, distribution, card_success, wallet_success, upi_success, bnpl_success)

def capture_transaction(transaction_id, capture_amount):
    if random.randint(1,100) <=15 and capture_amount >=300:
        capture_amount = capture_amount - random.randint(1,250)

    url = f"https://test-apis.boxpay.tech/v0/merchants/9Azy8efkWY/transactions/{transaction_id}/captures"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer P7rqu8r3kpIXOETMojVbE9eCkcnjl4YhLPFFGe33DPANvVAb1RH7J4x0Q091VnAp1fGHvbAvyAbGspY3iNCd1q",
        "X-Request-Id": "WFAFad"
    }
    
    data = {
        "money": {
            "amount": capture_amount,
            "currencyCode": "INR"
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        capture_response = response.json()
        print("Capture Response:", capture_response)
                
        if random.randint(1, 100) <= 70:
            refund_transaction(transaction_id, capture_amount)
                    
        return capture_response
        
    except Exception as e:
        return {"error": str(e)}
                
def refund_transaction(transaction_id,capture_amount):
    if random.randint(1,100) <=70:
        refund_amount = capture_amount
    else:
        refund_amount = round(capture_amount/random.randint(1,5))
    
       
    url = f"https://test-apis.boxpay.tech/v0/merchants/9Azy8efkWY/transactions/{transaction_id}/refunds"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer P7rqu8r3kpIXOETMojVbE9eCkcnjl4YhLPFFGe33DPANvVAb1RH7J4x0Q091VnAp1fGHvbAvyAbGspY3iNCd1q",
        "X-Request-Id": "fajksbdas77"  # You can generate a new request ID
    }
    
    data = {
        "money": {
            "amount": refund_amount,
            "currencyCode": "INR"
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        refund_response = response.json()
        print("Refund Response:", refund_response)
        
        return refund_response
        
    except Exception as e:
        return {"error": str(e)}



@app.route('/trigger', methods=['POST'])
def trigger_process():
    global api_processes, stop_event, stop_requested

    if not api_processes:
        
        api_url = request.json.get('api_url')
        api_key = request.json.get('api_key')    
          
        amount_args = request.json.get('amount', {})
        amount_floor = amount_args.get('amount_floor', 20)
        amount_ceiling = amount_args.get('amount_ceiling', 300)
        multiplier = amount_args.get('multiplier', 10)
       
        distribution = request.json.get('distribution', {
            "Card": 25,
            "Upi": 55,
            "Wallet": 10,
            "BuyNowPayLater": 10
        })
        
        success_rate_args = request.json.get('success_rate',{})
        card_success = success_rate_args.get('card_success',80)
        wallet_success = success_rate_args.get('wallet_success',80)
        upi_success = success_rate_args.get('upi_success',80)
        bnpl_success = success_rate_args.get('bnpl_success',80)
        
        num_instances = request.json.get('num_instances', 10)  # Number of instances to run

        for _ in range(num_instances):
            process = multiprocessing.Process(target=repeat_api_calls, args=(api_url, api_key, amount_floor, amount_ceiling, multiplier, distribution, card_success, wallet_success, upi_success, bnpl_success))
            api_processes.append(process)
            process.start()

        message = f"{num_instances} instances of API processing started."
        stop_event.clear()
        stop_requested = False  # Reset the stop_requested flag
        return jsonify({"message": message})

@app.route('/stop', methods=['POST'])
def stop():
    global api_processes, stop_event, stop_requested

    if api_processes:
        for process in api_processes:
            if process.is_alive():
                process.terminate()

        stop_event.set()
        api_processes = []  # Reset the list of processes
        stop_requested = True  # Set the stop_requested flag
        return jsonify({"message": "API processing stopped."})
    else:
        return jsonify({"message": "No processing to stop."})
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
