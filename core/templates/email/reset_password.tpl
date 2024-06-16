{% extends 'mail_templated/base.tpl' %}

{% block subject %}
forgot password
{% endblock %}

{% block html %}
<a class="form-label-link" href="http://{{ current_site }}{% url 'accounts:reset-password-check-token' token=token %}">password reset link"http://{{ current_site }}{% url 'accounts:reset-password-check-token' token=token %}"</a>

{% endblock %}
