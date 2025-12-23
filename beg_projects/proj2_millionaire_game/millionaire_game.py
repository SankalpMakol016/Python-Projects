questions = [
    [
        "What is the capital of India?",
        ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        1,
        1000
    ],
    [
        "Which language is used to write Python?",
        ["C++", "Java", "Python", "English"],
        3,
        2000
    ],
    [
        "Who is known as the Father of the Nation in India?",
        ["Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh", "Subhash Chandra Bose"],
        2,
        5000
    ],
    [
        "Which symbol is used for comments in Python?",
        ["//", "#", "/* */", "--"],
        2,
        10000
    ]
]

prize=0

for question in questions :
    print(f"Question is : {question[0]}")
    print("options are :")
    print(f"1.{question[1][0]}")
    print(f"2.{question[1][1]}")
    print(f"3.{question[1][2]}")
    print(f"4.{question[1][3]}")
    
    ans=int(input("Enter the correct option number: "))
    
    if(ans==question[2]):
        print("congratulation your answer is correct!!")
        prize+=question[3]
        print(f"your prize amount is {prize}")
    else:
        print("incorect answers...Better Luck Next Time")
        break
        
    