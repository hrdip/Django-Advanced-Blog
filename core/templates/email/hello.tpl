{% extends 'mail_templated/base.tpl' %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
This is an <strong> html </strong> message
<img src="https://buffer.com/cdn-cgi/image/w=1000,fit=contain,q=90,f=auto/library/content/images/size/w1200/2023/10/free-images.jpg">
{% endblock %}