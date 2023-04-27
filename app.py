from flask import Flask, request, jsonify

app = Flask(__name__)

usd = 11380.7 # 1 USD = 11380.7 UZS

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    args = request.args
    amount = args.get('amount', 0)
    usd = 11380.7
    to_usd = float(amount)/usd
    return jsonify({
                "amount": amount,
                "currency": "UZS",
                "converted": to_usd,
                "convertedCurrency": "USD"
            })


@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    args = request.args
    amount = args.get('amount', 0)
    to_uzs = usd*int(amount)
    return jsonify({
                "amount": amount,
                "currency": "USD",
                "converted": to_uzs,
                "convertedCurrency": "UZS"
            })

    

if __name__ == '__main__':
    app.run(debug=True)