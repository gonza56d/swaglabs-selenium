Feature: Payments

Scenario Outline: Payments
    When user fills the payment with the code <QR>

    Examples:
        | QR |
        | A  |
        | B  |
