{% extends 'mail_templated/base.tpl' %}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
"http://{{ current_site }}{% url 'accounts:activation' token=token %}"

{% endblock %}