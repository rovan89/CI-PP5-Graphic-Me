document.addEventListener('DOMContentLoaded', async () => {
    const stripe = Stripe('pk_test_51M1amaG7GfWqWKFm8y3AANp9eJ5YgtVx6l58p2p0x6pXDhlLA9zyRlq9WQTmGVo3nMAqcucyLj6m1kRSerF6Wf1h00ZupTZNZM')

    var elements = stripe.elements();
    var cardElement = elements.create('card');
    cardElement.mount('#card-element')
})