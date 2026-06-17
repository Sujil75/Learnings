#include <bits/stdc++.h>
using namespace std;

void pairArray() {
    pair<int, int> pairArr[] = {{1, 2}, {3, 4}, {5, 6}};
    
    cout << "Pair array method: pair<int, int> pairArr[] = {{1, 2}, {3, 4}, {5, 6}};" << endl; 
    for (int i=0; i < size(pairArr); i++) {
        cout << "Pair " << i + 1 << ": (" << pairArr[i].first << ", " << pairArr[i].second << ')' << endl;
    };
};

void pairSyntax() {
    cout << "Syntax: pair<int, char> p = {1, 'a'}" << endl;
};

void checkAndProvideChoiceFunction(int c) {
     switch(c) {
        case 1:
           pairSyntax();
           cout << endl;
           break;
        case 2:
            pairArray();
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
    string options[] = {"Syntax", "Pair Array"};
    optionsFunction(options, size(options));
    
    int choice;
    userChoice(choice);

    checkAndProvideChoiceFunction(choice);
    
    return 0;
};