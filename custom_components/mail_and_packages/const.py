DOMAIN = "mail_and_packages"
VERSION = "0.2.2-b5"
ISSUE_URL = "http://github.com/moralmunky/Home-Assistant-Mail-And-Packages"

# Configuration Properties
CONF_FOLDER = "folder"
CONF_PATH = "image_path"
CONF_DURATION = "gif_duration"
CONF_SCAN_INTERVAL = "scan_interval"
CONF_IMAGE_SECURITY = "image_security"
CONF_GENERATE_MP4 = "generate_mp4"

# Defaults
DEFAULT_NAME = "Mail And Packages"
DEFAULT_PORT = "993"
DEFAULT_FOLDER = '"INBOX"'
DEFAULT_PATH = "/home/homeassistant/.homeassistant/images/mail_and_packages/"
DEFAULT_IMAGE_SECURITY = True
DEFAULT_GIF_DURATION = 5
DEFAULT_SCAN_INTERVAL = 5
DEFAULT_GIF_FILE_NAME = "mail_today.gif"
DEFAULT_FFMPEG = False

# USPS
USPS_Mail_Email = "USPSInformedDelivery@usps.gov"
USPS_Mail_Subject = "Informed Delivery Daily Digest"
USPS_Packages_Email = "auto-reply@usps.com"
USPS_Delivering_Subject = "Expected Delivery on"
USPS_Delivered_Subject = "Item Delivered"
USPS_Body_Text = "Your item is out for delivery"

USPS_DELIVERED = "usps_delivered"
USPS_DELIVERING = "usps_delivering"
USPS_PACKAGES = "usps_packages"
USPS_TRACKING = "usps_tracking"

# UPS
UPS_Email = "mcinfo@ups.com"
UPS_Delivering_Subject = "UPS Update: Package Scheduled for Delivery Today"
UPS_Delivering_Subject_2 = "UPS Update: Follow Your Delivery on a Live Map"
UPS_Delivered_Subject = "Your UPS Package was delivered"
UPS_Body_Text = "Tracking Number"

UPS_DELIVERED = "ups_delivered"
UPS_DELIVERING = "ups_delivering"
UPS_PACKAGES = "ups_packages"
UPS_TRACKING = "ups_tracking"

# FedEx
FEDEX_Email = "TrackingUpdates@fedex.com"
FEDEX_Delivering_Subject = "Delivery scheduled for today"
FEDEX_Delivering_Subject_2 = "Your package is scheduled for delivery today"
FEDEX_Delivered_Subject = "Your package has been delivered"

FEDEX_DELIVERED = "fedex_delivered"
FEDEX_DELIVERING = "fedex_delivering"
FEDEX_PACKAGES = "fedex_packages"
FEDEX_TRACKING = "fedex_tracking"

# Amazon
Amazon_Domains = "amazon.com,amazon.ca,amazon.co.uk,amazon.in"
AMAZON_PACKAGES = "amazon_packages"
AMAZON_ORDER = "amazon_order"

# Canada Post
CAPost_Email = "donotreply@canadapost.postescanada.ca"
CAPost_Delivered_Subject = "Delivery Notification"

CAPOST_DELIVERED = "capost_delivered"
CAPOST_DELIVERING = "capost_delivering"
CAPOST_PACKAGES = "capost_packages"

# DHL
DHL_Email = "donotreply_odd@dhl.com"
DHL_Delivering_Subject = "DHL On Demand Delivery"
DHL_Delivered_Subject = "DHL On Demand Delivery"
DHL_Body_Text = "scheduled for delivery TODAY"
DHL_Body_Text_2 = "has been delivered"

DHL_DELIVERED = "dhl_delivered"
DHL_DELIVERING = "dhl_delivering"
DHL_PACKAGES = "dhl_packages"
DHL_TRACKING = "dhl_tracking"
