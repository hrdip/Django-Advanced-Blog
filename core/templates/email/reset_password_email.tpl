{% extends 'mail_templated/base.tpl' %}

{% block subject %}
forgot password
{% endblock %}

{% block html %}
http://{{current_site}}/{{realtivelink}}/{{uidb64}}/{{token}}

{% endblock %}