#include <bits/stdc++.h>
using namespace std;

void pairSyntax() {
    cout << "pair<int, char> p = {1, 'a'}" << endl;
};

void checkAndProvideChoiceFunction(int c) {
     switch(c) {
        case 1:
           pairSyntax();
           cout << endl;
           break;
        default:
            cout << "Provide a valid input" << endl;
            break;
    };
};

void userChoice(int &choice) {
    cout << "Your Choice Number: ";
    cin >> choice;

    cout << endl;
};

void optionsFunction(string options[], int n) {
    for (int i = 0; i < n; i++) {
        cout << i + 1 << ". " << options[i] << endl;
    };

    cout << endl;
};

int main() {
    cout << "Introduction to Pairs" << endl;

    cout << "Which option you need: " << endl;
    string options[] = {"Syntax"};
    optionsFunction(options, size(options));
    
    int choice;
    userChoice(choice);

    checkAndProvideChoiceFunction(choice);
    
    return 0;
};