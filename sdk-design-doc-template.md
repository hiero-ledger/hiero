# SDK Design Doc Template

Template for SDK design docs that will be checked into a SDK design docs repo.

## Summary

Brief description of the design, what it’s meant to accomplish, how it should be used, etc. Any information that would be relevant to the usage of the new design should be provided. Any changes to previous workflows that may result from the new design should be outlined. Links to relevant HIPs, protobuf PRs, services PRs, etc. should be provided here as well to provide additional context for the use of the new design. Links to relevant SDK/TCK issues/PRs should be provided as well.

## New APIs

Define the names of the new APIs being added, as well as how they are interacted with.

### New API #1

- `Type property` : description of the property.
    - Make note of any additional features to know about the property, such as min/max values, required/optional, etc.
    - Provide generic examples of setting/getting the property in code.
        - `NewApi setProperty(Type prop)`
        - `Type getProperty()`
- `NewApi function(Type1 var1, Type2 var2,...)` : description of what the function does.
    - Make note of any additional features/ramifications of using this function (anything that may not be immediately clear to the user).
    - `Type1 var1` : description of input variable.
        - Make note of any additional features to know about this input, such as min/max values, etc.
    - `Type2 var2` : description of input variable.

### New API #2

…

---

## Updated APIs

APIs that already exist in the SDKs that are getting updated in some way (generally fields are being added). A brief explanation of why the API is being updated as well should be provided.

### Updated API #1

- `Type newProperty` : description of the new property.
    - Make note of any additional features to know about the new property, such as min/max values, required/optional, etc.
    - Provide generic examples of setting/getting the new property in code.
        - `NewApi setProperty(Type prop)`
        - `Type getProperty()`
- `NewApi function(Type1 var1, Type2 var2,...)` : description of what the function does.
    - Make note of any additional features/ramifications of using this function (anything that may not be immediately clear to the user).
    - `Type1 var1` : description of input variable.
        - Make note of any additional features to know about this input, such as min/max values, required/optional, etc.
    - `Type2 var2` : description of input variable.

### Updated API #2

…

---

## Internal Changes

If applicable, description of any internal changes to the SDKs that may impact usage that don't involve an API change. It should describe why the change is happening and its relevancy to the feature. It should describe any new expected behavior and how it differs from old behavior, as well as how users should remedy the behavior chagne.

### Response Codes

If applicable, include any new consensus node response codes associated with this feature. Response codes are messages that the consensus node returns when a transaction succeeds or fails.
- `RESPONSE_CODE_1`
- `RESPONSE_CODE_2`
- ...

#### Transaction Retry

The SDK, in some cases, needs to understand when to retry on a given response code. Evaluate the new features and identify if there are specific cases the SDK may need to consider retrying. 

## Test Plan

Create a numbered list of end-to-end tests that should be implemented to fully test the new feature design. These should use the Given/When/Then idiom in order to fully define the test prerequisites and setup, what’s being tested, and the expected response. The tests should invoke all new response codes and validate them.

1. Given <prerequisites>, when <action>, then <result>.
2. Given <prerequisite #1>, <prerequisite #2>, and <prerequisite #3>, when <action>, then <result #1>, <result #2>, and <result #3>.
3. …

### TCK

The tests defined above should also be defined in the TCK repository. Issues should be created in the TCK repository based on this content to document all end-to-end tests and link it as reference in the design doc.

## SDK Example

Define an example that shows how to use the new feature in code. The example should follow the intended use case flow as defined in the HIP (i.e. user stories), and validate that this intended use case achieves the desired output. The example should define a list of steps which show the user case flow, and provide any checks and validations needed to show the desired output. If necessary, multiple examples can be provided and defined.

It it is deemed better, instead of defining a new example, to update an existing one, it should be stated what example is being updated and how. If more code is simply being added to the end of the example, the steps can simply be defined as if it was a new example and appended to the example. If, however, updating the example involves more complex changes, it may be best to redefine all the steps for the entire example.