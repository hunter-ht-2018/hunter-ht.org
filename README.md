# hunter-ht.org


### 环境
- Python2.7
- MySQL5.7+
- Ubuntu16.04+

### 部署步骤
- 首先下载或者克隆项目（hunter-ht.org或者自行重命名）
- 将项目文件夹放置于服务器目录下，并进入文件目录（hunter-ht.org）
- 设置环境变量MYSQL_USER和MYSQL_PASS，配置mysql数据库用户名和密码：
  ```
  export MYSQL_USER=XXX
  export MYSQL_PASS=XXX
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
> 若在使用过程中出现编码类问题报错，查看数据库中库/表/字段的编码方式；若编码方式非utf8/utf8mb4，修改数据库/表/字段编码方式为utf8/utf8mb4即可.

- 查看、更改数据库、表的编码格式：
- 查看数据库编码格式： show variables like 'character';
- 查看数据表的编码格式：show create table tablename;
- 修改数据库表的编码格式：ALTER TABLE tablename CHARACTER SET utf8mb4;
- 查看字段编码、字段类型：show full columns from tablename;
- 修改字段编码格式: ALTER TABLE tablename MODIFY COLUMN 字段名 字段类型 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ui;
- 重启数据库：service mysql restart
