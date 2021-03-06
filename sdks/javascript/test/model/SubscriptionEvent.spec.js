/**
 * ACES Listener API
 * API Specification for ACES Listeners that read data on a blockchain and forward transaction events to registered subscribers. 
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.AcesListenerApi);
  }
}(this, function(expect, AcesListenerApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AcesListenerApi.SubscriptionEvent();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('SubscriptionEvent', function() {
    it('should create an instance of SubscriptionEvent', function() {
      // uncomment below and update the code to test SubscriptionEvent
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be.a(AcesListenerApi.SubscriptionEvent);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "createdAt")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be();
    });

    it('should have the property tries (base name: "tries")', function() {
      // uncomment below and update the code to test the property tries
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be();
    });

    it('should have the property transactionId (base name: "transactionId")', function() {
      // uncomment below and update the code to test the property transactionId
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be();
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instane = new AcesListenerApi.SubscriptionEvent();
      //expect(instance).to.be();
    });

  });

}));
