# Strategy Design Pattern

The Strategy Design Pattern is a behavioral pattern that lets you define a family of algorithms, place each one in its own class, and make them interchangeable at runtime.

Instead of hardcoding multiple `if-else` or `switch` branches, the client chooses the behavior it wants and hands it to a context object.

## When to Use It

- You have multiple ways to perform the same task.
- You want to avoid large conditional blocks.
- You want to add new behaviors without changing existing code.
- You want to switch algorithms dynamically at runtime.

## Core Components

- Context: The class that uses a strategy object and delegates work to it.
- Strategy Interface: A common contract shared by all strategies.
- Concrete Strategies: The individual algorithm implementations.

## Example

Consider a shopping cart with multiple payment options:

- `PaymentStrategy` defines a common `pay()` method.
- `CreditCardStrategy`, `PayPalStrategy`, and `CryptoStrategy` each implement `pay()` differently.
- `ShoppingCart` receives a strategy and calls `pay()` without knowing the details.

This keeps payment logic separate from the cart and makes it easy to add new payment methods later.

## Benefits

- Removes complex conditional logic
- Follows the Open/Closed Principle
- Keeps algorithms isolated and reusable
- Makes behavior easy to swap at runtime

## Quick Summary

Use Strategy when the behavior may change and you want the code to stay flexible, clean, and easy to extend.
