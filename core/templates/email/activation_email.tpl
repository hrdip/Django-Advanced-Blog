{% extends 'mail_templated/base.tpl' %}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
http://{{current_site}}/{{realtivelink}}/{{token}}

{% endblock %}