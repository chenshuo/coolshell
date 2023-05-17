#!/bin/bash

echo $*

sed 's|https://coolshell.cn/articles/|/articles/|g' -i $*
sed 's|https://coolshell.cn/category/|/category/|g' -i $*
sed 's|https://coolshell.cn/cdn-cgi/scripts/|/cdn-cgi/scripts/|' -i $*
sed 's|https://coolshell.cn/favicon.png|/favicon.png|' -i $*
sed 's|https://coolshell.cn/page/|/page/|g' -i $*
sed 's|https://coolshell.cn/tag/|/tag/|g' -i $*
sed 's|https://coolshell.cn/wp-content/|/wp-content/|g' -i $*
sed 's|https://coolshell.cn/wp-includes/|/wp-includes/|g' -i $*
sed '/navbar-brand/s|https://coolshell.cn/|/|' -i $*
sed '/menu-item-17405/s|https://coolshell.cn/|/|' -i $*
sed '/menu-item-17406/s|https://coolshell.cn/featured|/featured|' -i $*
sed '/menu-item-17407/s|https://coolshell.cn/plugins|/plugins|' -i $*
sed '/menu-item-17408/s|https://coolshell.cn/guestbook|/guestbook|' -i $*
sed '/menu-item-17409/s|https://coolshell.cn/about|/about|' -i $*
sed '/menu-item-17410/s|https://coolshell.cn/haoel|/haoel|' -i $*

# TODO anti-baidu-latest.min.js
