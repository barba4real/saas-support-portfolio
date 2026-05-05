# API Integration Troubleshooting Checklist

This checklist is designed for first-line or technical support investigation before escalation.

## 1. Confirm the Customer's Goal

- What system is the customer trying to connect?
- What action should the integration perform?
- Is this a new setup or an existing integration that stopped working?
- Is the issue affecting one user, one account, or many users?

## 2. Check Environment and Endpoint

- Confirm whether the customer is using sandbox or production.
- Confirm the base URL.
- Confirm the endpoint path.
- Confirm the request method: GET, POST, PUT, PATCH, or DELETE.
- Confirm the API version.

## 3. Check Authentication

- API key or token is present.
- Token has not expired.
- Token belongs to the correct account/environment.
- Required scopes or permissions are enabled.
- Authorization header format is correct.

Example:

```http
Authorization: Bearer YOUR_TOKEN
Content-Type: application/json
```

## 4. Check Request Format

- Required fields are included.
- Field names match the API documentation.
- Data types are correct.
- JSON syntax is valid.
- Headers are correct.
- Query parameters are properly encoded.

## 5. Interpret Common Status Codes

| Status Code | Likely Meaning | Support Action |
| --- | --- | --- |
| 400 | Bad request or missing field | Review payload and required fields |
| 401 | Authentication failed | Check token/API key and auth header |
| 403 | Permission issue | Check account access and scopes |
| 404 | Endpoint/resource not found | Confirm URL, ID, and environment |
| 409 | Conflict or duplicate | Check existing records or state |
| 422 | Validation error | Review field values and format |
| 429 | Rate limit reached | Advise retry timing or escalation |
| 500 | Server-side issue | Collect evidence and escalate |

## 6. Postman Test Notes

**Request URL:**  
**Method:**  
**Headers checked:**  
**Payload checked:**  
**Response status:**  
**Response body summary:**  
**Result:**  

## 7. Escalation Note Template

Customer is experiencing an integration issue with [tool/system].

**Expected behavior:**  
**Actual behavior:**  
**Endpoint/method:**  
**Status code/error:**  
**Authentication checked:** Yes / No  
**Payload checked:** Yes / No  
**Steps reproduced:**  
**Customer impact:**  
**Suggested next step:**  

## 8. Customer-Friendly Response Template

Hi [Customer Name],

I reviewed the integration issue and checked the main configuration points, including authentication, endpoint setup, and request format.

The error appears related to [plain-language cause]. I have documented the findings and the next recommended step is [next action].

Best regards,  
Dave

