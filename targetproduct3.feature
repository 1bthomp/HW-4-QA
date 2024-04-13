1# Created by btxpr at 4/9/2024
Feature: Target Product Circle


  Scenario: User can navigate to the target home page
    Given Click on an item and add to cart
    When Check cart
    Then Go to cart
    And Verify item in cart