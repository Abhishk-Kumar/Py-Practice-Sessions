# code without class and with classs will be:

# name="OpenAI"
# model="gpt-4o-mini"

# def generate_response(prompt):
#     return response

# # with class 

# class OpenAIClient:
#     def __init__(self, name, model):
#         self.name=name
#         self.model=model

#     def generate_respons(prompt):
#         return respons


# __init__ is called dunder method its setup method for inital class 
class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

dog1=Dog("German sephard", "Golden retriever")
# passing with name 
dog2=Dog(name="German", breed="Goldie ")

print(dog1.breed)
print(dog2.name)


class APIConfig:
    def __init__(self, api_key, model="gpt-40-mini", max_tokens=500):
        self.api_key=api_key
        self.model=model
        self.max_tokens=max_tokens

dev_config=APIConfig("skdf_api_key", max_tokens=50)
prod_config=APIConfig(api_key="sd_key", model="gpt-3", max_tokens=40)

print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)


class APIClient:
    version = "1.0"              # Same for all clients
    max_retries = 3              # Same for all clients
    
    def __init__(self, api_key):
        self.api_key = api_key   # Unique to each client


class DataValidator:
    def __init__(self):
        self.errors=[]

    def validate_emails(self, email):
        if '@' not in email:
            print(f"Its a invalid email: {email} ")
            return False
        return True
    
    def validate_age(self, age):
        if age<0 or age>150:
            self.errors.append(f"Invalid age: {age}")
            print(f"Its a invalid email: {age} ")
            return False
        return True
    
    def get_errors(self):
       return self.errors
    

validator=DataValidator()

validator.validate_emails("abhishekgmail.com")
validator.validate_age(-2.5)

validator.validate_emails(email="abhismail.com")
validator.validate_age(age=200)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']



class Animal:
    def __init__(self, name):
        self.name=name

    def sleep(self):
        return f"{self.name} is sleeping"
    def eat(self):
        return f"{self.name} is eating"
    
class DOg(Animal):
    def bark(self):
        return f"{self.name} says bhow-bhow"
    
dog1=DOg("Abhishek")
dog2=DOg(name="abhay")

print(dog1.name)
print(dog1.sleep())
print(dog2.bark())