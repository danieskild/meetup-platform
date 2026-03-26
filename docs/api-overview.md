# API Overview

## Base URL
```
https://api.meetup-platform.com/v1
```

## Authentication
All endpoints require Bearer token authentication via OAuth 2.0.

```
Authorization: Bearer <access_token>
```

---

## Endpoints

### Scheduling
| Method | Endpoint | Description |
|---|---|---|
| GET | `/availability/{user_id}` | Get available slots |
| POST | `/bookings` | Create a new booking |
| PATCH | `/bookings/{id}` | Update a booking |
| DELETE | `/bookings/{id}` | Cancel a booking |

### Email
| Method | Endpoint | Description |
|---|---|---|
| POST | `/email/parse` | Parse a meeting invite |
| POST | `/email/send-confirmation` | Send meeting confirmation |
| POST | `/email/send-reminder` | Send meeting reminder |

### Conferencing
| Method | Endpoint | Description |
|---|---|---|
| POST | `/meetings/teams` | Create Teams meeting |
| POST | `/meetings/meet` | Create Google Meet |
| PATCH | `/meetings/{id}` | Update meeting room |
| DELETE | `/meetings/{id}` | Delete meeting room |

### Transport
| Method | Endpoint | Description |
|---|---|---|
| GET | `/transport/routes` | Get public transport routes |
| POST | `/transport/taxi` | Book a taxi |
| GET | `/transport/departure-time` | Calculate departure time |
| GET | `/transport/organized` | Get group transport options |
