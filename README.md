# hunter-ht.org
> **“Hunter-ht”文件夹即为项目所有代码**

### 环境
- Python2.7+
- MySQL5.7+
- Ubuntu16.04+

### 部署步骤
- 将项目文件“Hunter-ht”放置于服务器目录下
- 进入Hunter-ht目录
  ```
  cd Hunter-ht
  ```
- 执行如下两条命令，创建数据库
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- 运行
  ```
  python manage.py runsever 0.0.0.0:80 //自行指定端口
  ```
- 在浏览器中输入"IP:port"查看是否成功

### 注意事项
> 若在使用过程中出现编码类问题报错，查看数据库中库/表/字段的编码方式；若编码方式非utf8/utf8mb4，修改数据库/表/字段编码方式为utf8/utf8mb4即可.（建议后者）
