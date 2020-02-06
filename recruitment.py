def main():
    #write your code here
    skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
    cv = {}
    cv['name'] = input("What's your name? ")
    cv['age'] =int(input("How old are you? "))
    cv['experience'] =int (input("How many years of experience do you have? "))
    cv['skills'] = []

    print("Skills:")
    
    number = 1
    for skill in skills:
        print("{}. {}".format(number , skill))
        number +=1
    cv['skills'] =[int(input("Choose a skill from above by entering its number: "))]
    cv['skills'].extend([int(input("Choose another skill from above by entering its number: "))])

    if(6 in cv['skills']):
        if (cv['age'] >= 25 and cv['age'] < 40 and cv['experience'] > 5):
            print("accepted")
        else:
            print("rejected")
    else:
        print("rejected")


if __name__ == '__main__':
    main()
