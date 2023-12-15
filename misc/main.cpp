#include <iostream>

using namespace std;



int main()
{

    int listA[]={1721,979,366,299,675,1456};
    //long int a = ffind(listA);
    int arrSize = sizeof(listA)/sizeof(*listA);
    int i=0,check=0,result=0;
    while(i<=arrSize-1){
        check= 2020-listA[i];
        for(int j=arrSize-1;j>i;j--){
            if (check==listA[j]){
                result= listA[i]*listA[j];
                std::cout<<result<<endl;
            }
        }
        i++;

    }




    return 0;
}



