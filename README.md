# Commera Example App

A small Frappe app that shows how your own app can react to [Commera](https://github.com/bwhtech/commera) orders. It uses the three order hooks Commera offers:

- When an order is placed, it adds the comment "Commera Example App: order placed" to the Sales Order.
- When an order is fully paid, it adds the comment "Commera Example App: order paid".
- When a shopper tries to cancel an order tagged `Hold`, it refuses and tells them why.

Read `commera_example_app/hooks.py` and `commera_example_app/orders.py`. That is the whole app.

## Requirements

- A Frappe v16 bench with Commera installed.
- A Commera version that includes the order hooks. Until [bwhtech/commera#201](https://github.com/bwhtech/commera/pull/201) is merged, use its `feat/order-hooks` branch.

## Install

```bash
bench get-app https://github.com/Rl0007/commera_example_app
bench --site <site> install-app commera_example_app
```

Restart your workers afterwards so they pick up the new hooks.

## The hooks

Declare them in your app's `hooks.py` as lists of dotted paths.

| Hook | When it runs | Argument | What to return |
| --- | --- | --- | --- |
| `commera_order_placed` | After a shopper places an order | Sales Order name | Nothing |
| `commera_order_paid` | After an order is fully paid. For cash on delivery, only once the full amount is recorded | Sales Order name | Nothing |
| `commera_before_order_cancel` | Before a shopper's order is cancelled | Sales Order name | A translated reason to refuse, or `None` to allow |

A few things to know about `commera_order_placed` and `commera_order_paid`:

- Each runs once per order.
- They run in a background job, after the order has been saved, so they never slow down checkout.
- They run as Administrator, so check permissions yourself if you act on a user's behalf.
- If your handler raises, Commera logs it to Error Log and still runs the other handlers.

## Try it

1. Place a cash-on-delivery order from the storefront. Open the Sales Order in Desk: within a few seconds it has the comment "Commera Example App: order placed".
2. Submit the order, create its invoice and record a payment for the full amount. The order gets "Commera Example App: order paid".
3. Place another order, add the tag `Hold` to it in Desk, then try to cancel it from the shopper's account. It is refused with "This order is on hold, so it can't be cancelled." Remove the tag and the cancel goes through.

## License

MIT. Made by [BWH Tech](https://bwh.tech).
