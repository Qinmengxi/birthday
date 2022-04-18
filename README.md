# birthday-present
基于python+flask框架写的一个网页生日礼物

[博客连接](https://blog.csdn.net/zyh960/article/details/107687945)

## 1、使用ngrok让你的本地Flask程序外网可访问  
### 1.1 安装ngrok  
ngrok支持三大主流操作系统，安装流程比较简单，如下所示：  
- 访问https://ngrok.com/download  
- 根据操作系统下载对应的压缩包  
- 解压到合适的目录  

压缩包里包含一个名为ngrok的二进制文件，我们打开一个命令行窗口，切换到这个文件所在的目录。现在可以先执行help命令来测试一下。在Windows下，你可以使用下面的命令：  
ngrok http 5000
