# 今日内容

- 数据库
- 经典架构
  - LNMP
  - LAMP
  - LNMT

## 介绍

- NewSQL
  - googleSpanner
  - pingCAPTiDB
  - AliOceanBase

## Mysql发展史

![image-20190601100321034](../images/image-20190601100321034.png)

### 分支对比

![image-20190601100609129](../images/image-20190601100609129.png)
<<<<<<< HEAD

## 规划和安装

- yum安装

```
$ rpm -qa | grep mysql  # 检测是否安装mysql
$ rpm -e mysql　　       # 普通删除模式
$ rpm -e --nodeps mysql　# 强力删除模式，如果使用上面命令删除时，提示有依赖的其它文件，则用该命令可以对其进行强力删除
```

安装

```
$ wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
$ rpm -ivh mysql-community-release-el7-5.noarch.rpm
$ yum update
$ yum install mysql-server
```

权限设置：

```
$ chown mysql:mysql -R /var/lib/mysql
```

初始化 MySQL：

```
$ mysqld --initialize
```

启动 MySQL：

```
$ systemctl start mysqld
```

查看 MySQL 运行状态：

```
$ systemctl status mysqld
```

在成功安装 MySQL 后，一些基础表会表初始化，在服务器启动后，你可以通过简单的测试来验证 MySQL 是否工作正常。

使用 mysqladmin 工具来获取服务器状态：

使用 mysqladmin 命令俩检查服务器的版本, 在 linux 上该二进制文件位于 /usr/bin 目录，在 Windows 上该二进制文件位于C:\mysql\bin 。

```
$ mysqladmin --version
```

linux上该命令将输出以下结果，该结果基于你的系统信息：

```
> mysqladmin  Ver 8.23 Distrib 5.0.9-0, for redhat-linux-gnu on i386
```

如果以上命令执行后未输出任何信息，说明你的Mysql未安装成功。

Mysql安装成功后，默认的root用户密码为空，你可以使用以下命令来创建root用户的密码：

```
$ mysqladmin -u root password "new_password";
```

现在你可以通过以下命令来连接到Mysql服务器：

```
$ mysql -u root -p
Enter password:*******
```

