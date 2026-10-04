app_name = "commera_example_app"
app_title = "Commera Example App"
app_publisher = "BWH Tech"
app_description = "Example app showing how to hook into Commera orders"
app_email = "dev@bwh.tech"
app_license = "mit"

required_apps = ["commera"]

commera_events = {
	"order_placed": ["commera_example_app.orders.on_order_placed"],
	"order_paid": ["commera_example_app.orders.on_order_paid"],
}
commera_before_order_cancel = ["commera_example_app.orders.before_order_cancel"]
