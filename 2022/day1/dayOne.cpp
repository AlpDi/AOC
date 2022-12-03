#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main (){
    string line;
    ifstream inputFile, inputTestFile;
    ofstream outputFile;
    inputTestFile.open("inputTest.txt");
    inputFile.open("input.txt");
    outputFile.open("output.txt");


    int comp1 = 0;
    int comp2 = 0;
    int firstPlace = 0;
    int secondPlace = 0;
    int thirdPlace = 0;
    int compSwitch = 1;

    do{
        if(line.length() == 0 || inputFile.eof()){
            if(compSwitch == 1){
                compSwitch = 0;
                cout << comp1 << endl;
                comp1 > firstPlace ? firstPlace = comp1 : firstPlace = firstPlace;
                comp1 <= firstPlace && comp1 > secondPlace ? secondPlace = comp1 : secondPlace = secondPlace;
                comp1 < secondPlace && comp1 > thirdPlace ? thirdPlace = comp1 : thirdPlace = thirdPlace;
                comp1 = 0;
            } else {
                compSwitch = 1;
                cout << comp2 << endl;
                comp2 > firstPlace ? firstPlace = comp2 : firstPlace = firstPlace;
                comp2 < firstPlace && comp2 > secondPlace ? secondPlace = comp2 : secondPlace = secondPlace;
                comp2 < secondPlace && comp2 > thirdPlace ? thirdPlace = comp2 : thirdPlace = thirdPlace;
                comp2 = 0;
            }
        }
        else if(compSwitch == 1){
            comp1 += stoi(line);
        }
        else if(compSwitch == 0){
            comp2 += stoi(line);
        }
    }while(getline(inputFile, line));
    cout << firstPlace << " " << secondPlace << " " << thirdPlace << endl;
    cout << firstPlace + secondPlace + thirdPlace << endl;

    inputFile.close();
    outputFile.close();
}