/*
作者：不想起昵称（目前仅在B站发布视频）
搬运请标明原作者
有错误欢迎指出

原理讲解:
通过虚拟键盘按下左WIN键和D键，回到桌面。真的是非常的简单呢~
*/

#include <iostream> //导入基础库
#include <windows.h> //导入windows.h，用于休眠和按下虚拟键盘
#pragma comment(lib,"Advapi32.lib") //用于获取用户名
using namespace std; //命名空间
void start(){
    char strBuffer[256] ={0};
    DWORD dwSize = 256;
    GetUserName(strBuffer,&dwSize);
    //以上三行代码用于获取用户名
    cout << strBuffer << "?" << endl;
    Sleep(250);
    cout << "okay." << endl;
    Sleep(250);
    cout << "Do you know this is a computer virus? (Actually not a true computer virus, It to your computer's Harmfulness is not big)" << endl;
    Sleep(3000);
    cout << "If you don't, I give you five seconds to turn off the program." << endl;
    Sleep(2000);
    cout << "five ";
    Sleep(1000);
    cout << "four ";
    Sleep(1000);
    cout << "three ";
    Sleep(1000);
    cout << "two ";
    Sleep(1000);
    cout << "one" << endl;
    Sleep(1000);
    cout << "okay, It seems that you know." << endl;
    Sleep(1000);
    cout << "The virus is about to start." << endl;
    Sleep(1000);
    cout << "Bey :-)" << endl;
    Sleep(500);
    //以上全是警告
}

void VirusStart(){
    system("cls");//清屏
    char animation[4] = {'|', '\'', '-', '/'}; //创建一个字符列表
	for(int i=0;i<10;++i){ //有限循环
		for(int j=0;j<4;++j){ //嵌套循环
			system("cls"); //清屏
			cout << "Loading " << animation[j] << endl; //输出
			Sleep(50); //休眠50毫秒
		}
	}
	cout << "Done!" << endl; //输出
	Sleep(500); //休眠500毫秒
}

int main(){
    //start();
    //如果是整蛊请把上面的注释删掉
    ShowWindow(GetForegroundWindow(),0);//隐藏当前窗口
    while(1){
        keybd_event(VK_LWIN,0,0,0);//按下左WIN键
        keybd_event(68,0,0,0);//按下D键
        keybd_event(68,0,KEYEVENTF_KEYUP,0);//抬起D键
        keybd_event(VK_LWIN,0,KEYEVENTF_KEYUP,0);//抬起左WIN键
        Sleep(50);//休眠50毫秒
    }
    return 0; //返回0
}
