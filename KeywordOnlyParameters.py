""":keyword only parameters
just as function may specify positional only paramaters before
a backslash(\) in the paramter lists, a ffunction may specify
keyword only paramaters  by placing an asterisk * in the paramter list
subsequent arguments must be passed as keywords arguments
Afunctional parameters *args can receieve any number of arguments
must place keyword only arguments after positional arguments
if last parameter in a function's parameter list is **kwargs,
function may receieve any arbitrary number of arguments
    used for function that receive any number of arguments
    cases in which some keywords are optional
    Intepreter places extra keywords arguments in dictionay and passes it to kwargs
    """
#function below only uses keywords only paramters
#it receievs required and optional keywords
#* begins, no required position keywords, **kwargs no potential keywords argument
#sender and receipient will be required
def send_mail(*, sender,recipient, **kwargs):
    print(f'Sending {sender} to Recipient: {recipient}')
    #display the optional keywords if any
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')
    else:
        print(f'No additional arguments passed to {sender}')
answer4 = send_mail(sender ="Emily", recipient= "Alan")
print(answer4)
answer5 = send_mail(sender ="Emily", recipient= "Alan",
                    subject="Testing the engine",
                     body="please the car has the problem with engine")
print(answer5)

#dictionary unpacking operators
paramters = {
    "sender" : "Emily@gmail.com",
    "recipient" : "DanielatheGirl@gmail.com",
    "subject" : "Bring me apple juice",
    "body" : "Costco has the best apple juice to drink,"
             "i will bring you one",
    'cc':"Alan@gmail.com",
    'bcc':"Alan1@gmail.com"
}
"""use ** dictionay unpacking operators to extract the paramtwer key-value pairs
"""
paramter = send_mail(**paramters)
print(paramter)