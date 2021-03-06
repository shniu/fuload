/*=============================================================================
#  Author:          dantezhu - http://www.vimer.cn
#  Email:           zny2008@gmail.com
#  FileName:        fl_slave_input.cpp
#  Description:     
#  Version:         1.0
#  LastChange:      2010-11-28 21:11:25
#  History:         
=============================================================================*/
#include "fl_slave_input.h"

int CFLSlaveInput::SetInputData(const string& strInputData)
{
    m_LastInputData = strInputData;
    return parseInputData(m_LastInputData);
}
int CFLSlaveInput::parseInputData(const string& strInputData)
{
    m_SWInputRoute.clear();

    string tempInputData = strInputData;
    tempInputData = CFLCommFunc::replace_all(tempInputData,"\r\n","\n");

    vector<string> vecLines;
    CFLCommFunc::SplitString(tempInputData,"\n",vecLines);

    int loopNum = 1;
    foreach(vecLines,it)
    {
        string tempLine = *it;

        if (tempLine.size()<=0)
        {
            continue;
        }

        if(tempLine[0] != ' ' && tempLine[0] != '\t')//证明是suite说明
        {
            if (tempLine[0] == '#')//这是注释
            {
                continue;
            }

            size_t begin_index = tempLine.find("[");
            if (begin_index == string::npos)
            {
                loopNum = 1;
                continue;
            }
            size_t end_index = tempLine.find("]",begin_index);
            if (end_index == string::npos)
            {
                loopNum = 1;
                continue;
            }
            if (begin_index == end_index)
            {
                loopNum = 1;
                continue;
            }

            string substr = tempLine.substr(begin_index+1,end_index-begin_index-1);
            loopNum = atoi(substr.c_str());
            continue;
        }

        tempLine = CFLCommFunc::StripString(tempLine);

        if (tempLine.size()<=0)
        {
            continue;
        }

        StSWInput swi;
        vector<string> vecParams;
        CFLCommFunc::SplitString(tempLine,"&",vecParams);

        map<string,string> mapParams;
        string tempStr;
        foreach(vecParams,vecIt)
        {
            tempStr = *vecIt;
            vector<string> t_vec;
            CFLCommFunc::SplitString(tempStr,"=",t_vec);
            if (t_vec.size()!=2)
            {
                return -4;
            }
            mapParams[CFLCommFunc::StripString(t_vec[0])] = CFLCommFunc::StripString(t_vec[1]);
        }

        swi.mapParams = mapParams;
        swi.strInputLine = tempLine;
        m_SWInputRoute.add(swi,loopNum);
    }
    return 0;
}
int CFLSlaveInput::Alloc(StSWInput& node)
{
    return m_SWInputRoute.alloc(node);
}
