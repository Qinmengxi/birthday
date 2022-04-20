# birthday-present
基于python+flask框架写的一个网页生日礼物,参考[博客](https://blog.csdn.net/zyh960/article/details/107687945)

## 1、使用ngrok让你的本地Flask程序外网可访问  
### 1.1 安装ngrok  
ngrok支持三大主流操作系统，安装流程比较简单，如下所示：  
- 访问https://ngrok.com/download  
- 根据操作系统下载对应的压缩包  
- 解压到合适的目录  

注：本仓库已下载ngrok.exe，其余操作系统需要自己下载  

### 1.2 建立映射/HTTP隧道
压缩包里包含一个名为ngrok的二进制文件，我们打开一个命令行窗口，切换到这个文件所在的目录。现在可以先执行help命令来测试一下。在Windows下，你可以使用下面的命令： 
- ngrok config add-authtoken 27vGDS620MSpbSXgWZTH822meax_4UTkzxAM79wmYewYu9QLY（第一次需要注册，在https://dashboard.ngrok.com/get-started/setup可见）
- ngrok http 5000  

```
ngrok
Session Status                online  
Account                       Qinmengxi (Plan: Free)  
Version                       3.0.2  
Region                        Asia Pacific (ap)  
Latency                       96.6491ms  
Web Interface                 http://127.0.0.1:4040  
Forwarding                    https://5e3d-2409-8a00-da5-c890-c405-e59b-632c-cc1f.ap.ngrok.io -> http://localhost:5000  
Connections                   ttl     opn     rt1     rt5     p50     p90  
                              0       0       0.00    0.00    0.00    0.00  
```

其中的 https://5e3d-2409-8a00-da5-c890-c405-e59b-632c-cc1f.ap.ngrok.io 就是为你分配的可以外部访问的网址，所有发向这个网址的请求都会转发到你的本地机5000端口，即localhost:5000或127.0.0.1:5000。
