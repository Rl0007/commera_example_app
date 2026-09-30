import frappe
from frappe import _

HOLD_TAG = "Hold"


def on_order_placed(sales_order: str) -> None:
	add_order_comment(sales_order, _("Commera Example App: order placed"))


def on_order_paid(sales_order: str) -> None:
	add_order_comment(sales_order, _("Commera Example App: order paid"))


def before_order_cancel(sales_order: str) -> str | None:
	user_tags = frappe.db.get_value("Sales Order", sales_order, "_user_tags") or ""
	# Desk stores tags as one comma-separated string with a leading comma, e.g. ",Hold,VIP"
	if HOLD_TAG in user_tags.split(","):
		return _("This order is on hold, so it can't be cancelled.")
	return None


def add_order_comment(sales_order: str, content: str) -> None:
	frappe.get_doc("Sales Order", sales_order).add_comment("Comment", content)
