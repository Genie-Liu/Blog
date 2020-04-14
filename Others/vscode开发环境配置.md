# VSCode配置

## 通用配置

1. vim插件

    插件平台里面搜vim，第一个即可。配置使用相对行号`"editor.lineNumbers": "relative"`，这样就不用计算相对行数了
2. 字体

    有很多常用字体可以选，我这边常用的有以下几个：[Fira Code](https://github.com/tonsky/FiraCode), Source Code Pro, Consolas;
    
    字体大小我比较喜欢细一些，所以设置了200

    ```javascript
    "editor.fontFamily": "Fira Code, Source Code Pro, Consolas, 'Courier New', monospace",
    "editor.fontSize": 16,
    "editor.fontLigatures": true,
    "editor.fontWeight": "200",
    ```
3. 主题

    我这边用的solarized light

## 特定语言

### python

1. 格式化：

    使用yapf的google stype配置, 缩进改为2（python太容易超过pep8的长度导致分行了）

    ```javascript
    "python.formatting.yapfArgs": [
        "--style",
        "{based_on_style: chromium, indent_width: 2}"
    ],
    ```

