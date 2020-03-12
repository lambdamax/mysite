from rest_framework import serializers
from .models import  Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('name', 'body', 'visited', 'catalog',
                  'recommand', 'active', 'order_id',
                  'tags')


# class LmtbCustSerializer(serializers.ModelSerializer):
#     address = LmtbCustAddressesSerializer(many=False, read_only=True)
#     class Meta:
#         model = LmtbCust
#         fields = ('cust_cd', 'cust_entity_cd', 'cust_name', 'cust_reg_grp_cd', 'cust_contact_person',
#         'cust_subgrp_cd', 'cust_reporting1', 'cust_reporting2', 'cust_search_str',
#         'address', 'cust_subgrp_cd', 'cust_sales_rep')