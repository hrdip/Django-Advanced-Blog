{% extends 'mail_templated/base.tpl' %}

{% block subject %}
forgot password
{% endblock %}

{% block html %}
http://127.0.0.1:8000/accounts/api/v1/password-reset/{{uidb64}}/{{token}}

{% endblock %}