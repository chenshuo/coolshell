# Static mirror of CoolShell.cn

<https://coolshell.org>

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

* <https://github.com/ghostincoolshell/haoel-articles>
* <https://github.com/soulteary/forever-coolshell>

