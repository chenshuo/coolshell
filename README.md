# Static mirror of CoolShell.cn

<https://coolshell.org>

## In Memoriam of haoel@

Dennis M. Ritchie 逝世十多年后，他的个人主页仍然能正常访问 <https://www.bell-labs.com/usr/dmr/www/>

W. Richard Stevens 已经逝世二十余年，他的个人主页还保持着 1999 年的样子 <http://www.kohala.com/start/>

希望借助 GitHub，让陈皓的文字能长久流传下去。

## Convert (most) links to local

```shell
$ shopt -s globstar
$ sed 's|https://coolshell.cn/articles/|/articles/|g' -i **/*.html
$ sed 's|https://coolshell.cn/category/|/category/|g' -i **/*.html
$ sed 's|https://coolshell.cn/tag/|/tag/|g' -i **/*.html
$ sed 's|https://coolshell.cn/wp-content/|/wp-content/|g' -i **/*.html
$ sed 's|https://coolshell.cn/wp-includes/|/wp-includes/|g' -i **/*.html
$ sed '/navbar-brand/s|https://coolshell.cn/|/|' -i **/*.html
$ sed '/menu-item-17405/s|https://coolshell.cn/|/|' -i **/*.html
$ sed '/menu-item-17406/s|https://coolshell.cn/featured|/featured.html|' -i **/*.html
$ sed '/menu-item-17407/s|https://coolshell.cn/plugins|/plugins|' -i **/*.html
$ sed '/menu-item-17408/s|https://coolshell.cn/guestbook|/guestbook|' -i **/*.html
$ sed '/menu-item-17409/s|https://coolshell.cn/about|/about|' -i **/*.html
$ sed '/menu-item-17410/s|https://coolshell.cn/haoel|/haoel|' -i **/*.html
```

## Other sites

* <https://github.com/ghostincoolshell/haoel-articles> 包括 tweets 和微博
* <https://github.com/soulteary/forever-coolshell> 单机下载版

