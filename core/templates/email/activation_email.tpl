{% extends 'mail_templated/base.tpl' %}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
<a class="form-label-link" href="http://{{ current_site }}{% url 'accounts:activation' token=token %}">activation link</a>

{% endblock %}