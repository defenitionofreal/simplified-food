from apps.sms.models.sms_log import SmsLog
from apps.sms.models.enums.status import Status

from django.contrib.auth import get_user_model
from enum import Enum

import requests
import os
import re

User = get_user_model()


class SmsProvider(Enum):
    SMS_AERO = "SMS_AERO"
    TWILIO = "TWILIO"


class SmsBaseHelper:

    def __init__(self, provider: SmsProvider):
        if not isinstance(provider, SmsProvider):
            raise ValueError('Invalid provider')
        self.provider = provider

    def send_sms(self, to_phone: str, message: str) -> bool:
        """ """
        if self.provider == SmsProvider.TWILIO:
            base_url = os.environ.get("SMS_AERO_API_URL", None)
            account_sid = os.environ.get("TWILIO_SID")
            auth_token = os.environ.get("TWILIO_TOKEN")
            url = f"{base_url}/Accounts/{account_sid}/Messages.json"
            data = {
                "From": "bla bla",
                "To": to_phone,
                "Body": message
            }
            response = requests.post(
                url, data=data, auth=(account_sid, auth_token)
            )

            if response.status_code == 201:
                res = response.json()
                user = User.objects.filter(phone=to_phone).first()
                SmsLog.objects.create(
                    sms_id=res["sid"],
                    text=res["body"],
                    status=Status.SENT,
                    recipient_id=user.id if user else None,
                    phone=to_phone
                )
                return True
            else:
                res = response.json()
                user = User.objects.filter(phone=to_phone).first()
                SmsLog.objects.create(
                    sms_id=res["code"],
                    text=res["message"],
                    status=Status.FAILED,
                    recipient_id=user.id if user else None,
                    phone=to_phone
                )
                return False

        return False



