#include <iostream>

void foo(char *letters, unsigned int size) {
    for(int V=1; V<20; V++) {
        std::cout << "\n========================   " << V <<"   ============================\n";
        int j = 0;
        int k = 0;
        for(int i=0; i<size; i++) {
            if(j*V >= size) {
                j = 0;
                k++;
            }
            std::cout << letters[(j*V)+k];
            j++;
        }
        int aux;
        std::cin >> aux;
    }
}

int main()
{
    std::string input = "", aux;
    while(std::cin >> aux){
        if(aux=="END_ENCRYPTED_TEXT") break;
        input = input + aux;
    }
    std::cout << "Input size: " << input.size() << std::endl;
    char letters[input.size()];
    unsigned int i = 0;
    for(char letter : input) {
        letters[i] = letter;
        i++;
    }
   
    foo(letters, input.size());

    return 0;
}