# 5.a. Any other comments on network connectivity?

Respondents agree that network connectivity should be tightly controlled to avoid failures of information governance, such as leakage of sensitive data from a TRE or even between workspaces within a TRE. But configurability is key. The needs of different projects vary widely, and while some may operate well without requiring network connectivity either outside or within the TRE, others may not. And as noted by one respondent, the relationship between network connectivity and contractual relationships between the data owners and those who require access to the data can be complex. Thus, the precise configuration of network connectivity may need to be decided on a case-by-case basis, which implies that a TRE should be configurable to suit the circumstances.

Network connectivity to resources outside the TRE should be restricted by default. However, there are many cases in which access to external resources may be useful or even essential. Access to external software repositories such as CRAN/PyPi is typically perceived as desirable, if not essential. Connectivity to allow import of project-specific code or data into a workspace may also be desirable. However, these needs may be met by an ingress procedure that does not require direct connectivity to the external resource from within the TRE (e.g. an airlock procedure mediated by TRE administrators). In general, it is desirable that a mechanism exists by which access to external resource can be provided on a project-by-project level, subject to information governance policy.

Some respondents express the position that external resources should also be TRE-like, or at least known and trusted. Again, this may vary on a case-by-case basis. Others note that external connectivity would be required for access to federated analytics services, which in principle should protect data privacy while allowing access to advanced computational resources.

Network connectivity within a TRE should be considered to enable collaboration, which several respondents considered to be essential. Again, this should be tightly controlled so as not to allow data leakage between workspaces. Thus, for example, users within a specific workspace should be able to collaborate and share code or data between themselves, but should not be able to link that data to datasets from outside that workspace. Projects should typically be isolated from one another.

# 21. Additional technical features: describe other technical features we may have missed and how important they are.

The responses to this this question were quite difficult to summarise. Many respondents raised individual potential features. Some of those may be representable in the specification, whereas others reflect more fine-grained potential configurations of a specific individual TRE. A common topic was general quality-of-life enhancements to user (both researcher and admin/PI) experience, such as automation of many processes. Other comments reflected specific security concerns.

Some degree of self-service is seen as desirable and a way of decreasing overall admin burden. For example, providing deployable templates for specific features, allowing users to automatically request desired resources could be useful. Similarly, self-service and automated management of users and projects might help reduce overall administrative burdens.

Many comments suggested that transparency and visibility of usage may be useful - for example, allowing users, administrators, or project PIs to see stats on costs, running processes, general workspace and storage use.

A break-glass feature allowing an appropriate person to stop running processes in the event that they are "runaway" or shutting down some capacities in the event of a ongoing security breach may also be helpful.

Some suggestions were around built-in quality management tools that would allow assessment of compliance with relevant standards (e.g. 5 Safes), with automated checking of system configurations.

A further consideration raised was for the needs of a federation of TREs.

Several respondents commented on risks surrounding data leakage. For example, some suggested that tools for automatically or manually assessing the risk of statistical disclosure would be useful. Similar tools might also include methods of generating synthetic datasets that might be more readily shared for exploratory research. Others focussed on different aspects of security, such as restricting access based on physical location or to specific networks.

Some respondents raised specific technologies for encryption and enhancement of privacy.

# 22. Additional comments: share any other thoughts and feelings on technical features.

There was some overlap in themes with the responses to questions 5 and 21. Some comments fell outside of the intended scope of the question, but are nevertheless potentially relevant to the specification.

Many respondents felt that balance between security and usability needs to be struck, and that it may be important to ensure that a TRE is not overly-engineered and complex to administer or use. Flexibility to adapt to local needs and IG norms is required. Specific features could be mapped on to well-defined use cases to justify inclusion of those features. One respondent argued that having high confidence in the security of the environment and prevention of unauthorised data egress is paramount, and flexibility must be secondary to that aim.

Comments on logging were mixed - while logging might allow usage patterns to be monitored and potentially allow "abnormal" activity to be spotted as a potential security breach/risk, another respondent felt that logging is largely of forensic value only, is mostly unused, and that proper risk management would ameliorate the need for logging.

While the value of automatic updates is recognised, there were some concerns that their automatic application might break some workflows or present unexpected security risks, and thus some degree of manual oversight of updates may be necessary.

Some respondents felt that the survey overlooked the needs of data curators and engineers, whose primary role may not be research or administration directly. These users main role may be to make data compatible with IG and optimised for analysis. These users may also need further access to different types of storage currently unmentioned in the specification.

Some comments expressed that on-premise TREs needed further consideration, and that even on-premise TREs could be managed using infrastructure as code.

One respondent expressed that oversight of ingress and egress of software should be considered two separate roles, as the assessment of risk is quite different. Similarly, another felt that there should be differentiation between TRE admins and trusted third parties or project admins.

Several respondents raised points around backups and archiving. One felt that the location of the backups - e.g. offsite - might raise information governance issues. Another raised that while backup is mentioned, restoring from backups is not - should users be allowed to restore? Another suggested that workspaces should be archivable.

Some TRE systems follow a "remote-jobs" model, in which researchers supply code which is then used remotely within a TRE; the researchers thus never access the data directly. Some respondents expressed skepticism, stating that this approach relies on excellent data curation and its suitability is limited for exploratory research or low quality data.

# 23.a. Are there sensitivity systems that you think are important or use?

The responses to this question can be broadly summarised as falling into two camps:
- All data should be treated as at the highest level of sensitivity
- The security level of a TRE should be configurable

The former camp views tiering or sensitivity systems as adding an unnecessary layer of complexity. Instead, the focus should be on "excellent data stewardship" and TREs should protect all data maximally. Because of difficulties in determining how sensitive data truly is, it may be best to treat all data as maximally sensitive. Others report that local information governance policy mandates that all data be treated with the highest level of security.

The latter camp instead argues that it is not necessary for all data and situations to be treated equally. The level of security might depend on the needs of the organisation and be determined by local policy. A TRE that is able to accommodate such variability is better able to be adapted to a specific local environment. A typical example would be that clinicians might need and be allowed access to fuller datasets than researchers, who could be restricted only to data required for their specific research purpose. But given appropriate controls, both could access the data through the same system.

The majority of responses fell in the "flexible" camp. In principle, the flexible approach allows for maximal security to be applied where necessary, whereas the "all maximum" approach cannot accommodate flexibility. Given the brevity of the comments, it is not clear that sensitivity and security were used in the same way by all respondents.

# 24.a. Additional aspects of governance: Briefly describe other aspects of governance we may have missed and how important they are.

Multiple respondents expressed the need for clear standardised guidelines, policies and procedures, and the need for training in all of these areas.

The need for training was repeated by many respondents. This training could differ according to the needs of different users, but could also be tied to specific standards, with the possibility of access being revoked if users fail to maintain those standards. A specific example given was the need to encourage researchers to properly consider the need for data security, particularly from backgrounds where the nature of personal information is not typically considered.

One suggestion was that appropriate training might result in user "passports" allowing access to multiple TREs.

Standardisation of user roles was also suggested by multiple respondents. Those user roles could align with specific policy requirements on a per project basis.

One respondent noted that there may be a tradeoff between institutional and individual standards. While asserting individual researcher's standards through training and quality assurance is one thing, the trustworthiness of the organisation through which they work or that holds the data may also be an issue to be considered.

# 25. Additional comments: share any other thoughts and feelings on policies and processes.

Respondents generally agreed that standardisation of policies and processes would be important and useful. Having simple, clear, relatable standards facilitates collaboration and makes it easier to explain why specific limits on user behaviour exist. Indeed, one respondent considered policies and processes more important than deciding on the technical infrastructure, as the latter must be designed to comply with the former.

Important points raised by several respondents are with respect to the potential impact of standardisation on accreditation. As they point out, existing processes of validating that a person is a "safe person" under the 5 Safes framework are likely to be specific to a given TRE. But having standardised processes and policies may facilitate granting of access to multiple TREs, if the agreed standards are shared between them. Specific examples might relate to attaining comparable legal documentation in different countries or legal domains, and recognising them across those domains - i.e. interoperable governance principles. In addition, having a standardised set of policies and process may facilitate accreditation by existing data owners, funding bodies, or TREs.

Several respondents raised the concern that overly restrictive or complex policies and processes might be problematic. The majority of users are domain experts, and having relatively low barriers to entry might improve adoption of appropriate practice. The need for balance between security and flexibility is emphasised. An example of flexibility might be that for some data, admin oversight need not be manual at all times. Instead, automated checks (such as malware/virus scanning) could be performed with data owners required to check that the contents of their file shares are appropriate periodically. Allowing streaming data ingress from trusted sources may be important in many research settings, as opposed to ad-hoc occasional manual transfer.

Another suggestion was that given that the configuration of many aspects of TREs can be specific to the needs of the client or organisation, a set of suggested standard configurations that cover the most common circumstances would be useful. Along similar lines, another respondent suggested that providing guidelines as to how many and what type of staff might be required to run TREs of different levels of complexity and size.
