from django.urls import path
from .views import check_pending_transactions, delete_cart, delete_transaction, get_transaction_by_hash, get_transaction_order_items, save_cart, register_transaction, update_transaction, generate_invoice, get_user_transactions, get_cart, clear_cart

urlpatterns = [
    # path('verify-signature', verify_signature, name='verify_signature'),
    # path('transaction-details', transaction_details, name='transaction_details'), 
    path('register-transaction', register_transaction, name='register_transaction'),  
    path('update-transaction/<int:transaction_id>', update_transaction, name='update_transaction'),  
    path('delete-transaction/<int:transaction_id>', delete_transaction, name='delete-transaction'),    
    path('generate-invoice/<int:transaction_id>', generate_invoice, name='generate_invoice'),   
    path('get-user-transactions/<str:wallet_address>', get_user_transactions, name='get_user_transactions'),     
    path('check-pending-transactions/<str:wallet_address>/', check_pending_transactions, name='check_pending_transactions'),    
    # path('transaction-details/<str:tx_hash>', get_transaction_details, name='transaction_details'),
    path('get-transaction-by-hash/<str:tx_hash>', get_transaction_by_hash, name='get_transaction_by_hash'),
    path('get-transaction-order-items/<int:transaction_id>', get_transaction_order_items, name='get_transaction-order-items'),
    path('save-cart', save_cart, name='save_cart'),       
    path('get-cart/<str:wallet_address>/', get_cart, name='get_cart'),       
    path('clear-cart/<str:wallet_address>', clear_cart, name='clear_cart'),       
    path('delete-cart/<str:wallet_address>', delete_cart, name='delete_cart'),       
]

