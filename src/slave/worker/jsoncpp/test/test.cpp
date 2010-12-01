#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include "json/json.h"
using namespace std;
int main(int argc, const char *argv[])
{

    string httpcontent = "{\"userid\":\"woaini\"}";

    Json::Reader reader;
    Json::Value value;
    std::string param;
    param.assign(httpcontent.c_str(), httpcontent.size());
    if (!reader.parse(param, value))
    {
        printf("json parse err, param: %s", param.c_str());
        return -1;
    }
    string userid = value["userid"].asString();
    cout<<userid<<endl;
    return 0;
}
