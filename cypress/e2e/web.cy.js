describe('Web tests', () => {
  
  it('should visit the home page', () => {
    cy.visit('/')
    cy.get('.title').should('have.text', 'Comidas favoritas')
    // cy.get('.flex-item').click()
    // cy.get('.flex-item').click({ multiple: true})
    // cy.click('.w3-button')
  })

  it ('should open the menu and its options', () => {
    cy.visit('/')
    // Opens food option 
    cy.get('.menu').click()
    cy.get('#food').click()
    cy.url().should('include', '/home#food')
    // Open about me option
    cy.get('.menu').click()
    cy.get('#about').click()
    cy.url().should('include', '/home#about')
  })
})